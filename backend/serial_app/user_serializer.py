from rest_framework import serializers
from django.contrib.auth import get_user_model


#this serializer is used for adding new users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'email', 'last_name', 'department', 'school', 'school_short_form', 'set_year', 'password']

    def create(self, validated_data):
        get_user_model().objects.create_user(**validated_data)


#this serializer is used to display user information to the public
class UserSerializerDisplay(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'department', 'school', 'set_year']






#trying to avoid circular import
from .group_serializer import  B3GroupSerializerShowGroupDetail
from .post_serializer import PostsSerializer
from .application_serializer import ApplicationSerializerDisplay


#this serializer is used to show the user his private information
class UserSerializerPrivate(serializers.ModelSerializer):
    #created groups
    groups_created = B3GroupSerializerShowGroupDetail(many=True)
    #sub admin groups
    group_sub_admins = B3GroupSerializerShowGroupDetail(many=True)
    #posts
    writter = PostsSerializer(many=True)
    #applications submitted
    user_applying = ApplicationSerializerDisplay(many=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'department', 'school', 'set_year', 'groups_created', 'group_sub_admins', 'writter', 'user_applying', 'currently_managing']



#serializer for all the users posts
class UserPostsSerializer(serializers.ModelSerializer):
    writter = PostsSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'department', 'school', 'set_year', 'writter']



#serializer to show the user all his created groups
class ViewUserCreatedGroupsSerializer(serializers.ModelSerializer):
    #created groups
    groups_created = B3GroupSerializerShowGroupDetail(many=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'department', 'school', 'set_year', 'groups_created']



#serializer to show the user all the group he is an admin of
class ViewUserAdminGroupsSerializer(serializers.ModelSerializer):
    #sub admin groups
    group_sub_admins = B3GroupSerializerShowGroupDetail(many=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'department', 'school', 'set_year', 'group_sub_admins']


