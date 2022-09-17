
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from serial_app.user_serializer import UserSerializer
from rest_framework import status
from creator_apis.tasks import welcome_mail

# Create your views here.
@api_view(['GET'])
def HomeView(request):
    return Response({'status':True})

class CreateUser(APIView):
    def post(self, request):
        validate_data = UserSerializer(data=request.data)
        if validate_data.is_valid():
            try:
                validate_data.save()
            except:
                Response(status=status.HTTP_501_NOT_IMPLEMENTED)

            #extract the email
            get_mail = str(validate_data.data.get('email'))
            e_mail = [get_mail]
            #send the success mail async
            welcome_mail.delay(e_mail)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



