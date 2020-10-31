from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .models import UserAccount
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework import viewsets


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 




