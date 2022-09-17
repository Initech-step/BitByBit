from rest_framework.views import APIView
from rest_framework.response import Response
from serial_app.application_serializer import (ApplicationSerializerAcceptOrDecline, ApplicationSerializerDisplay, ApplicationSerializer)

from serial_app.subscribers_serializer import B3SubscribersSerializer, AddSubscribersSerializer

from serial_app.user_serializer import (UserSerializer, UserSerializerDisplay, UserSerializerPrivate, UserPostsSerializer, ViewUserCreatedGroupsSerializer, ViewUserAdminGroupsSerializer)

from serial_app.settings_serializer import SetMesaageSerializer

from serial_app.post_serializer import PostsSerializer, AddPostSerializer

from serial_app.group_serializer import (B3GroupPostsSerializer, B3GroupSerializerDisplay, B3GroupSerializerShowGroupDetail, B3GroupSerializer)

from rest_framework import status, authentication
from rest_framework.permissions import IsAuthenticated
from auth_api.models import B3Groups, Applications, B3Subcribers, Posts

import json
from django.contrib.auth import get_user_model
from .tasks import send_newsletter, new_subscriber_letter







# Create your views here.
class CreateGroup(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        get_user_info = request.user
        validate_data = B3GroupSerializer(data=request.data)

        if validate_data.is_valid():
            #get and edit group attributes
            group_to_create = validate_data.data
            group_to_create['group_creator'] = get_user_info
            #save
            group = B3Groups(**group_to_create)
            group.save()
            #add the creator as a group admin
            group.group_admins.add(get_user_info)
            return Response(validate_data.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)




class ToggleApplication(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user_info = request.user
        #making sure we have what we need in the request
        try:
            state = request.data['state']
            print(request.data, state)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        #check if user currently managing is set
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)
        try:
            group = B3Groups.objects.get(pk=user_info.currently_managing)
        except:
            return Response({'status':False, 'message':'Error! Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        #change active status
        if state == "on":
            group.is_open_for_application = True
            group.save()
        elif state == "off":
            group.is_open_for_application = False
            group.save()
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':True, 'admission_state': group.is_open_for_application}, status=status.HTTP_202_ACCEPTED)


class SetCurrentlyManagingGroup(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, group_id):
        user_info = request.user
        #get group
        try:
            group = B3Groups.objects.get(pk=group_id)
        except:
            return Response({'status':False, 'message':'Group does not exist'})
        #check if requested user is group creator
        if user_info != group.group_creator:
            return Response({'status':False, 'message':'You are not the group creator'}, status=status.HTTP_403_FORBIDDEN)
        #edit currently managing
        user_info.currently_managing = group.id
        user_info.save()
        return Response({'status':True, 'currently_managing': group.id}, status=status.HTTP_200_OK)




class ApplyForAdmin(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_info = request.user
        validate_data = ApplicationSerializer(data=request.data)
        if validate_data.is_valid():
            #pass the data into a variable for modification
            modify = validate_data.data
            #get the group id and check
            group_id = modify.get('b3_group')
            try:
                group = B3Groups.objects.get(pk=group_id)
            except:
                return Response({'status':False, 'message':'Group does not exist'})

            #check if the group is accepting applications
            if group.is_open_for_application == False:
                return Response({'status':False, 'message':'This group is not recieving applications'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                
            #add neccessary data
            modify['b3_group'] = group
            modify['applicant'] = user_info
            #make the application
            apply = Applications.objects.create(**modify)
            apply.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class ViewApplications(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    #to view all applications to the currently managed groups
    def get(self, request):
        user_info = request.user
        #check if currently managing is set
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)
        #check for group existence
        try:
            group = B3Groups.objects.get(pk=user_info.currently_managing)
        except:
            return Response({'status':False, 'message':'Error! Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # get all applications
        filtered_applications = Applications.objects.filter(b3_group=group)
        data = ApplicationSerializerDisplay(filtered_applications, many=True)
        return Response(data.data)


    #to accept application
    def post(self, request):

        validate_data = ApplicationSerializerAcceptOrDecline(data=request.data)
        user_info = request.user

        #check for currently managing
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

        g_to_match = B3Groups.objects.get(pk=user_info.currently_managing)

        #validate data
        if validate_data.is_valid():
            #get application obj
            application_id = validate_data.data.get('id')
            try:
                application_obj = Applications.objects.get(pk=application_id)
            except:
                Response(status=status.HTTP_404_NOT_FOUND)

            #get group attached to applicatiopn
            group_obj = application_obj.b3_group

            #CHECK IF IT THE CURRENTLY MANAGED GROUP i.e if group attached to application is the one currently managed.
            if group_obj != g_to_match:
                return Response({'status':False}, status=status.HTTP_428_PRECONDITION_REQUIRED)

            applicant = application_obj.applicant

            #add applicant to group sub admin
            group_obj.group_admins.add(applicant)
            
            #delete the application from the db
            application_obj.delete()

            return Response(status=status.HTTP_200_OK)
            #add that user to 
        return Response(status=status.HTTP_400_BAD_REQUEST)

        
        


class ViewGroupsOpenForApplication(APIView):
    #logic: check for all groups that their open for application is true
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        groups_open = B3Groups.objects.filter(is_open_for_application=True)
        colate = B3GroupSerializerDisplay(groups_open, many=True)
        return Response(colate.data)




#get group data
class ViewGroupDetailPublic(APIView):
    #get the group Id and send back data
    #send back the data with number of posts
    def get(self, request, group_id):
        try:            
            group = B3Groups.objects.get(pk=group_id)
        except:
            return Response({'status':False, 'message':'Group does not exist'})
        colate = B3GroupSerializerShowGroupDetail(group)
        return Response(colate.data)



# used for searching groups
class SearchGroups(APIView):
    def get(self, request):
        quer = dict(request.query_params)
        try:
            search_axis = quer['axis'].pop(0)
            search_text = quer['search_text'].pop(0)
            print(search_text)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if search_axis == 'group_name':
            result = B3Groups.objects.filter(group_name__icontains=search_text)
            colate = B3GroupSerializerDisplay(result, many=True)
            return Response(colate.data)
        elif search_axis == 'group_school':
            result = B3Groups.objects.filter(group_school__icontains=search_text)
            colate = B3GroupSerializerDisplay(result, many=True)
            return Response(colate.data)
        else:
            result = B3Groups.objects.filter(group_department__icontains=search_text)
            colate = B3GroupSerializerDisplay(result, many=True)
            return Response(colate.data)




class ViewMyProfilePublic(APIView):
    def get(self, request, user_id):
        try:
            user_info = get_user_model().objects.get(pk=user_id)
        except:
            return Response({'status':False, 'message':'Error! User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        colate = UserSerializerDisplay(user_info)
        return Response(colate.data)
        

class ViewMyProfilePrivate(APIView):
    #get the user
    #retieve all things to do with that user including Posts, groups, applications
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_info = request.user
        collate = UserSerializerPrivate(user_info)
        return Response(collate.data)




class ViewAllSubAdmins(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_info = request.user

        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

        currently_managing = user_info.currently_managing

        group_info = B3Groups.objects.get(pk=currently_managing)
        group_sub_admins = group_info.group_admins.all()
        colate = UserSerializerDisplay(group_sub_admins, many=True)
        return Response(colate.data, status=status.HTTP_200_OK)




class SetMessageForNewlyAcceptedApplicant(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_info = request.user
        validate_data = SetMesaageSerializer(data=request.data)
        if validate_data.is_valid():
            if user_info.currently_managing == None or user_info.currently_managing == "":
                return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

            currently_managing = user_info.currently_managing
            group_info = B3Groups.objects.get(pk=currently_managing)

            group_info.message_for_accepted_applicant = validate_data.data.get('message')
            group_info.save()
            return Response(status=status.HTTP_202_ACCEPTED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class SetMessageForNewSubscribers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_info = request.user
        validate_data = SetMesaageSerializer(data=request.data)
        if validate_data.is_valid():

            if user_info.currently_managing == None or user_info.currently_managing == "":
                return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

            currently_managing = user_info.currently_managing
            group_info = B3Groups.objects.get(pk=currently_managing)

            group_info.message_for_new_subscriber = validate_data.data.get('message')
            group_info.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class ViewMyCreatedGroups(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_info = request.user
        collate = ViewUserCreatedGroupsSerializer(user_info)
        return Response(collate.data)




class ViewMyManagedGroups(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_info = request.user
        collate = ViewUserAdminGroupsSerializer(user_info)
        return Response(collate.data)




class ExpelSubAdmin(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def post(self, request, admin_id):

        user_info = request.user
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

        currently_managing = user_info.currently_managing
        group_info = B3Groups.objects.get(pk=currently_managing)
        #check if such admin exists as a user
        try:
            admin_info = get_user_model().objects.get(pk=admin_id)
        except:
            return Response({'status':False, 'message':'Admin doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)
        #initiate expulsion process
        group_info.group_admins.remove(admin_info)
        return Response(status=status.HTTP_202_ACCEPTED)



#view all the posts that relates to a user
class ViewAllMyPosts(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_info = request.user
        collate = UserPostsSerializer(user_info)
        return Response(collate.data)





class ViewAllPostForMyCreatedGroup(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_info = request.user
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

        currently_managing = user_info.currently_managing
        group_info = B3Groups.objects.get(pk=currently_managing)
        colate = B3GroupPostsSerializer(group_info)
        return Response(colate.data)



class SendNewsletter(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request, group_id):
        #get user data
        user_info = request.user
        #check if passed in group exists
        try:            
            group = B3Groups.objects.get(pk=group_id)
        except:
            return Response({'status':False, 'message':'Group does not exist'})

        #validate data sent
        validate_data = AddPostSerializer(data=request.data)
        if validate_data.is_valid():
            #check if user is an admin or subadmin
            authorized_personnel = group.group_admins.all()
            #check if user is admin
            if user_info in authorized_personnel:
                collate = validate_data.data
                if user_info == group.group_creator:
                    #add with approved
                    collate['b3_group'] = group
                    collate['approved'] = True
                    collate['written_by'] = user_info
                    send_posts = Posts.objects.create(**collate)
                    send_posts.save()

                    #prepare mails
                    prepared_mails = []
                    for recipient in group.subscribers.all():
                        prepared_mails.append(str(recipient.email))
                    
                    #send mails
                    send_newsletter.delay(
                        group_name=group.group_name,
                        post_title=collate['letter_title'],
                        body=collate['body'],
                        recipients=prepared_mails
                    )
                    return Response({'status':True, 'message':'Emails on the way'}, status=status.HTTP_201_CREATED)
                else:
                    #add without approved
                    collate['b3_group'] = group
                    collate['approved'] = False
                    collate['written_by'] = user_info
                    send_posts = Posts.objects.create(**collate)
                    send_posts.save()
                    return Response(status=status.HTTP_201_CREATED)
            else:
                print('You are not authorized, get out')
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        





class SubscribeToGroup(APIView):
    def post(self, request):

        #get and validate
        validate_data = AddSubscribersSerializer(data=request.data)
        if validate_data.is_valid():
            #check if group exists
            try:
                group = B3Groups.objects.get(pk=validate_data.data['b3_group'])
            except:
                return Response({'status':False, 'message':'Error! Group does not exist'}, status=status.HTTP_404_NOT_FOUND)
            # add to subscribers
            B3Subcribers.objects.create(email=validate_data.data['email'], b3_group=group)
            #get the email
            new_subscriber = [validate_data.data['email']]
            
            #get the group message for new subscribers
            message = str(group.message_for_new_subscriber)

            #execute task to mail the subscriber
            new_subscriber_letter.delay(new_subscriber, message)
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class UserHasCurrentlyManaging(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_info = request.user
        #check if user has currently managing
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'msg': 'User does not have currently managing'})
        try:            
            group = B3Groups.objects.get(pk=user_info.currently_managing)
        except:
            return Response({'status':False, 'message':'Group does not exist'})

        collate = B3GroupSerializerShowGroupDetail(group)
        return Response({'status': True, 'group_data': collate.data})















class ViewPostsPendingApproval(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_info = request.user

        #check if user has currently managing
        if user_info.currently_managing == None or user_info.currently_managing == "":
            return Response({'status':False, 'message':'We expect currently managing to be set'}, status=status.HTTP_417_EXPECTATION_FAILED)

        currently_managing = user_info.currently_managing
        #get the group
        try:
            group_info = B3Groups.objects.get(pk=currently_managing)
        except:
            return Response({'status':False, 'message':'Group doesnt exist'}, status=status.HTTP_404_NOT_FOUND)
        #get all posts belonging to that group and is not approved
        pending_posts = Posts.objects.filter(b3_group=group_info).filter(approved=False)
        collate = PostsSerializer(pending_posts, many=True)
        return Response(collate.data)



#approve post
class ApprovePost(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def put(self, request, post_id):
        print('in')
        #get the user
        user_info = request.user

        #get the post and make sure it a valid post
        try:
            post = Posts.objects.get(pk=post_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print('user info', user_info)
        print('creator', post.b3_group.group_creator)

        if user_info != post.b3_group.group_creator:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        #get group related to post
        group_info = post.b3_group

        #get all the subscribers of that group
        subscribers = B3Subcribers.objects.filter(b3_group=group_info)
        
        #approve
        post.approved = True
        post.save()

        #send out mails
        prepared_mails = []
        for recipient in subscribers:
            prepared_mails.append(str(recipient.email))
        print(prepared_mails)
                    
        #send mails
        send_newsletter.delay(
            group_name=group_info.group_name,
            post_title=post.letter_title,
            body=post.body,
            recipients=prepared_mails
        )
        return Response({'status':True, 'message':'Emails on the way'}, status=status.HTTP_202_ACCEPTED)