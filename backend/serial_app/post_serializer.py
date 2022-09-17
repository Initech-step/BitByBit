from rest_framework.serializers import ModelSerializer
from auth_api.models import Posts, B3Groups
from serial_app.user_serializer import UserSerializerDisplay


class SpecialB3GroupSerializerDisplay(ModelSerializer):
    class Meta:
        model = B3Groups
        fields = '__all__'




class PostsSerializer(ModelSerializer):
    #for displaying posts
    written_by = UserSerializerDisplay()
    class Meta:
        model = Posts
        fields = '__all__'


class AddPostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ('body', 'letter_title')
    