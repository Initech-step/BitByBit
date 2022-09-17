from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class SetMesaageSerializer(serializers.Serializer):
    #for accepting or declining
    message = serializers.CharField(max_length=2000)
