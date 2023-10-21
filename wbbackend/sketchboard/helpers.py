from django.conf import settings
import requests
import random
import json

def send_otp_to_phone(phone_number):
    try:
        otp=random.randint(1000,9999)
        print("api: ",settings.API_KEY)
        url=f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}'
        response=requests.get(url)
        return otp
       
        
    except:
        print("Exception occurred in sending otp")
        return None