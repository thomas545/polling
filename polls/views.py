from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                    CreateAPIView, ListAPIView,
                                    RetrieveAPIView, DestroyAPIView
                                                                    )
from rest_framework.response import Response
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
from.models import Poll, Choice, Vote
from django.contrib.auth import authenticate

# Create your views here.

class CreateUserAPIView(CreateAPIView):
    permission_classes = ('IsAuthenticated',)
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user :
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class PollListApiView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        data1 = PollSerializer(polls, many=True).data
        return Response(data1)


class PollDetailAPIView(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)


class PollListCreateAPIView(ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class ChoiceListAPIView(ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


class VoteListAPIView(ListCreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
