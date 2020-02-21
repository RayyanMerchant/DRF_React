from django.shortcuts import render
from .models import Post, Calc
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CalcSerializer
from rest_framework.authentication import TokenAuthentication

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)

class CalcViewSet(viewsets.ModelViewSet):
    queryset = Calc.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CalcSerializer
    authentication_classes = (TokenAuthentication,)
