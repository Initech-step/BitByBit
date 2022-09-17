
from rest_framework.serializers import ModelSerializer
from auth_api.models import B3Subcribers

class B3SubscribersSerializer(ModelSerializer):
    class Meta:
        model = B3Subcribers
        fields = ('email',)

class AddSubscribersSerializer(ModelSerializer):
    class Meta:
        model = B3Subcribers
        fields = ('email', 'b3_group')


