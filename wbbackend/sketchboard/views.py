from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .helpers import send_otp_to_phone
from .serializers import UserSerializer
# Create your views here.
class index(APIView):
    def get(self,request):
        return Response({'message':"success"})
    
class Register(APIView):
    def post(self,request):
        data=request.data
        print("data> ",data)
        phone_number=data.get('phone_number')
        password=data.get('password')
        if phone_number is None:
            return Response({
                'status':400,
                'message':'Phone number is required'
            })
        if password is None:
            return Response({
                'status':400,
                'message':'password is required'
            })
        
        user=User.objects.create_user(phone_number=data.get('phone_number'),otp=send_otp_to_phone(data.get('phone_number')))
       
        return Response({'status':200,'message':'User Registration Successful'})
    
class VerifyOTP(APIView):
    def post(self,request):
        data=request.data
    
        if data.get('phone_number') is None:
             return Response({
            'status':400,
            'message':'key phone_number is required'
        })
    
        try:
            user_object=User.objects.get(phone_number=data.get('phone_number'))
        except Exception as e:
            return Response({
                'status':400,
                'message':'invalid phone number'
                
            })
        if user_object.otp==data.get('otp'):
            user_object.is_phone_verified=True
            user_object.save()
            return Response({'status':200,'message':'OTP matched'})
        else:
            return Response({
                'status':400,
                'message':'invalid otp'
                
            })
        