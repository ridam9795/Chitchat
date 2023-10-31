from django.contrib.auth.hashers import make_password,check_password
from .models import User


class PhoneAuthenticationBackend(object):
    @staticmethod
    def authenticate(request, username=None, password=None):
        try:
            user = User.objects.get(phone_number=username)

        except User.DoesNotExist:
            return None

        if user and check_password(password,user.password):
            return user

        return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None