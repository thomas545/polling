from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path('create/user/', views.CreateUserAPIView.as_view(), name='user'),
    path('login2/', views.LoginView.as_view(), name='login2'),
    path('poll-list/', views.PollListCreateAPIView.as_view(), name='list'),
    path('choice-list/', views.ChoiceListAPIView.as_view(), name='list_choise'),
    path('vote-list/', views.VoteListAPIView.as_view(), name='list_vote'),
    path('poll/<int:pk>', views.PollRetrieveAPIView.as_view(), name='detail_poll'),
]
