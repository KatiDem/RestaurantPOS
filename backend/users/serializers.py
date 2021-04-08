from rest_framework import serializers
from .models.custom_user import *
from .models.admin import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class AdminSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='customuser.id')
    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects)
    user = CustomUserSerializer(many=False)

    class Meta:
        model = Admin
        fields = '__all__'

