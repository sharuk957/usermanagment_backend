from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets,parsers
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import MyUser
from .serializer import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class UserRegistrationView(CreateAPIView):

    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]





class UserManagmentView(viewsets.ModelViewSet):

    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]
    http_method_names = ['get','patch','delete']
    authentication_classes =  [JWTAuthentication]
    permission_classes     =  [IsAuthenticated]




class LoginView(APIView):

        def post(self,request):
            email = request.data.get('email')
            password = request.data.get('password')
            print(password)
            if MyUser.objects.filter(email=email).first():
                user = authenticate(email=email,password=password)

                if user is None:
                    return Response({'message':'invalid Credential'},status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'message':'Invalid email'},status=status.HTTP_401_UNAUTHORIZED)
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                'access': str(refresh.access_token)
                })
