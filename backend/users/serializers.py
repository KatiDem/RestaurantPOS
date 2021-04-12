from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models.custom_user import *
from .models import CustomUser, Admin, Cook, Waiter
from django.contrib.auth import get_user_model
UserModel = get_user_model()

# class CustomUserCreateSerializer(UserCreateSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}
# class CustomUserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = UserModel
#         fields = ('email', 'first_name', 'last_name', 'password',
#                   'phone_number', 'is_admin', 'is_cook', 'is_waiter',)

class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'first_name', 'last_name', 'password',
                  'phone_number', 'is_admin', 'is_cook', 'is_waiter',)


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number',)


class AdminProfileSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='customuser.id')
    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects)
    # user = CustomUserSerializer(many=False)
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = Admin
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class AdminProfileCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        exclude = ['created_at', 'updated_at', ]


class CookProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = Cook
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class CookProfileCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        exclude = ['created_at', 'updated_at', ]


class WaiterProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = Waiter
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class WaiterProfileCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        exclude = ['created_at', 'updated_at', ]

class CustomUserWithProfileSerializer(UserSerializer):
    admin_profile = AdminProfileSerializer(read_only=True, source='admin')
    cook_profile = CookProfileSerializer(read_only=True, source='cook')
    waiter_profile = WaiterProfileSerializer(read_only=True, source='waiter')

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name',
                  'phone_number',
                  # 'is_admin', 'is_cook', 'is_waiter',
                  'admin_profile', 'cook_profile', 'waiter_profile'
                  ]