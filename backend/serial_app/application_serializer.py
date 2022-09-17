from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from auth_api.models import Applications

class ApplicationSerializerAcceptOrDecline(serializers.Serializer):
    #for accepting or declining
    id = serializers.IntegerField()


class ApplicationSerializerDisplay(ModelSerializer):
    #for displaying applications
    class Meta:
        model = Applications
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):
    #this is for adding the application
    class Meta:
        model = Applications
        fields = ('application_message', 'b3_group')
