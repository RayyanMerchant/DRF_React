from django.shortcuts import render
from .models import Post, Calc
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CalcSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)


@api_view(['GET', 'POST'])
def CalcView(request):
    if request.method == 'GET':
        calcs = Calc.objects.all()
        serializer = CalcSerializer(calcs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CalcSerializer(data=request.data)
        if serializer.is_valid():
            res = int(serializer.data['num1']) + int(serializer.data['num2'])
            obj = Calc(num1=serializer.data['num1'], 
            num2=serializer.data['num2'], 
            newid=serializer.data['newid'], 
            result = res,
            )
            obj.save()
            newdic = serializer.data
            newdic['result'] = res
            return Response(newdic, status=status.HTTP_201_CREATED)


