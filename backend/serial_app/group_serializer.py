from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import post_serializer
from .subscribers_serializer import B3SubscribersSerializer
from auth_api.models import B3Groups, Posts


class B3GroupPostsSerializer(ModelSerializer):
    posts = post_serializer.PostsSerializer(many=True, source='filtered_posts')
    class Meta:
        model = B3Groups
        fields = ('group_name', 'group_description', 'group_department', 'group_school', 'posts')



#for seeing all groups
class B3GroupSerializerDisplay(ModelSerializer):
    class Meta:
        model = B3Groups
        fields = '__all__'


#avoid circular import
########################
from serial_app.user_serializer import UserSerializerDisplay
########################


#for getting group detail of a particular group
class B3GroupSerializerShowGroupDetail(ModelSerializer):
    group_creator = UserSerializerDisplay()
    group_admins = UserSerializerDisplay(many=True)
    subscribers = B3SubscribersSerializer(many=True)
    class Meta:
        model = B3Groups
        fields = ('id', 'group_name', 'group_description', 'group_department', 'group_school', 'group_creator', 'group_admins', 'subscribers')




#for adding groups
class B3GroupSerializer(ModelSerializer):
    class Meta:
        model = B3Groups
        fields = ('group_name', 'group_description', 'group_department', 'group_school')