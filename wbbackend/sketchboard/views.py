from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .helpers import send_otp_to_phone
from django.contrib.auth import login,authenticate
from django.conf import settings
from django.middleware import csrf
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.
class index(APIView):
    def get(self,request):
        return Response({'message':"success"})
    
class Register(APIView):
    def post(self,request):
        data=request.data
        print("data> ",data)
        name=data.get("name")
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
      
        try:
            user=User.objects.get(phone_number=data.get('phone_number'))
            return Response({'status':409,'message':'User Already Exist'})
        except User.DoesNotExist:
            user=User.objects.create_user(phone_number=data.get('phone_number'),otp=send_otp_to_phone(data.get('phone_number')))
            user.first_name=name
            user.save()
            return Response({'status':200,'message':'User Registration Successful'})
    
class VerifyOTP(APIView):
    def post(self,request):
        data=request.data
        print(data)
        if data.get('phone_number') is None:
             return Response({
            'status':400,
            'message':'phone_number is required'
        })
    
        try:
            user_object=User.objects.get(phone_number=data.get('phone_number'))
            print(user_object)     
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
 
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    user = User.objects.get(phone_number=user.phone_number)
    
     
    return {
        'name': user.first_name,
        'phone_number':user.phone_number,
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }        
class Login(APIView):
    def post(self,request):
        data=request.data
        phone_number=data.get('phone_number')
        password = data.get('password')

        if phone_number is None:
            return Response({
                'message':'Phone number is required',
                'status':400
            },status=status.HTTP_400_BAD_REQUEST)
            
        if password is None:
            return Response({
                'message':'password is required',
                'status':400
            },status=status.HTTP_400_BAD_REQUEST )
      
      
        try:
            user=User.objects.get(phone_number=data.get('phone_number'))
        except Exception as e:
            return Response({
                'message':'User does not exists,please register'  ,
                'status':404   
            },status=status.HTTP_404_NOT_FOUND)
        # if not user.is_phone_verified:
        #     return Response({
        #         'message':'Please verify mobile number',
        #         'status':401     
        #     },status=status.HTTP_401_UNAUTHORIZED)
        response = Response()

        if user.is_active:
            data = get_token_for_user(user)

            response.set_cookie(
                key=settings.SIMPLE_JWT["AUTH_COOKIE"],
                value=data['access'],
                expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = {"status":200,"Success": "Login Successfully", "data": data}
            return response
        else:
            return Response({'status':401,"No active": "This account is not active!!"}, status=status.HTTP_401_UNAUTHORIZED)
        
class SearchUser(APIView):
    def get(self,request,format=None):
        phone_number=request.query_params.get("phone_number")
        user=User.objects.get(phone_number=phone_number)
        userSerializer=UserSerializer(user)
        return Response({"status":200,"user":userSerializer.data},status=status.HTTP_200_OK)
        
    