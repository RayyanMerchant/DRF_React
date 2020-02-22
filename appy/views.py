from django.shortcuts import render
from .models import Calc, Student, Assignment
from rest_framework import viewsets, permissions
from .serializers import CalcSerializer, StudentSerializer, AssignmentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json


@api_view(['POST', ])
def HostelView(request):
    if request.method == 'POST':
        print(request.data)
        return Response({"a" : "A"}, status=status.HTTP_201_CREATED)

@api_view(['POST'],)
def AssignmentIDView(request):
    if request.method == 'POST':
        id = request.data.__getitem__('id')
        req_assignment = Assignment.objects.filter(id=id).first()
        serializer = AssignmentSerializer(req_assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST','GET',])
def PendingTaskView(request):
    if request.method == 'POST':
        print("request.data = ", request.data)
        print("request.data.__getitem__('email') = ", request.data.__getitem__('email'))
        email = request.data.__getitem__('email')
        cur_student = Student.objects.filter(email=email).first()
        pending_assignment = Assignment.objects.filter(student=cur_student, done=False)
        serializer = AssignmentSerializer(pending_assignment, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def AssignmentView(request):
    if request.method == 'POST':
        print("fdfsfds = ", request.method)
        serializer = AssignmentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print(serializer.data)
            task = serializer.data['task']
            submission_date = serializer.data['submission_date']
            content = serializer.data['content']
            qs = Student.objects.all()
            for cur in qs:
                obj = Assignment(task=task, submission_date=submission_date, student=cur, content=content)
                obj.save()
                print(obj, " ", type(obj))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def StudentView(request):
    pass


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


