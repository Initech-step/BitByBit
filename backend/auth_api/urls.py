
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.HomeView, name='index'),
    path('create_user/', views.CreateUser.as_view()),
    path('get_token/', obtain_auth_token)
]