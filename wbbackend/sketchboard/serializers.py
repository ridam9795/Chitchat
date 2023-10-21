from rest_framework import serializers
from .models import Chat,Group,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'