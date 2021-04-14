from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import generics, status, response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import NotFound

from drf_spectacular.utils import extend_schema, OpenApiParameter

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer, \
    TokenRefreshSerializer

from .models import User
from utils.errors import ErrorSerializer
from .serializers import UserSerializer, PasswordChangeSerializer, PasswordResetSerializer, \
    PasswordResetConfirmSerializer, MyTokenObtainPairSerializer

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password', 'new_password_confirm'
    )
)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


@method_decorator(name='post', decorator=extend_schema(
    description='Returns a token and a refresh token for valid credentials',
    responses={
        200: TokenObtainPairSerializer,
        400: ErrorSerializer,
        401: ErrorSerializer,
    }
))
class TokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@method_decorator(name='post', decorator=extend_schema(
    description='Returns a token if the refresh token is valid',
    responses={
        200: TokenRefreshSerializer,
        400: ErrorSerializer,
        401: ErrorSerializer,
    }
))
class TokenRefreshView(jwt_views.TokenRefreshView):
    pass


class UserViewSet(generics.RetrieveAPIView,
                  generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user

    @method_decorator(name='retrieve', decorator=extend_schema(
        description='Get Auth User',
        responses={
            200: UserSerializer,
            401: ErrorSerializer,
        }
    ))
    def get(self, request, *args, **kwargs):
        current_user = self.get_object()
        serializer = self.get_serializer(current_user)
        return response.Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        current_user = self.get_object()
        serializer = self.get_serializer(instance=current_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if getattr(current_user, '_prefetched_objects_cache', None):
            current_user._prefetched_objects_cache = {}
        return response.Response(serializer.data)

    @method_decorator(name='update', decorator=extend_schema(
        description='Partially update Auth User',
        responses={
            200: UserSerializer,
            400: ErrorSerializer,
            401: ErrorSerializer,
            404: ErrorSerializer,
        }
    ))
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [JWTAuthentication]

    @method_decorator(name='post', decorator=extend_schema(
        description='Reset password',
        responses={
            200: PasswordResetSerializer,
            400: ErrorSerializer,
            404: ErrorSerializer,
        }
    ))
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.data['email']).first()

        if not user:
            raise NotFound(detail='An account with this email does not exist!')
        else:
            serializer.save()
        return Response(
            {"detail": _("Password reset e-mail has been sent.")},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (permissions.AllowAny,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    @method_decorator(name='post', decorator=extend_schema(
        description='Reset password confirm',
        responses={
            200: PasswordResetConfirmSerializer,
            400: ErrorSerializer,
        }
    ))
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": _("Password has been reset with the new password.")}
        )


class PasswordChangeView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    @method_decorator(name='post', decorator=extend_schema(
        description='Set password Auth user',
        responses={
            200: PasswordChangeSerializer,
            400: ErrorSerializer,
            401: ErrorSerializer,
        }
    ))
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password "
                                     "has been saved and e-mail "
                                     "has been sent.."
                                     )})
