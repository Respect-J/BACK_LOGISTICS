from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserCreateSerializer
from django.utils.crypto import get_random_string
from django.conf import settings


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False  # Initially inactive until email verification
            verification_code = get_random_string(length=5, allowed_chars='0123456789')

            # Store the code in the user's session or database
            user.verification_code = verification_code
            user.save()

            # Send the email
            send_mail(
                subject='Email Verification Code',
                message=f'Your verification code is: {verification_code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

            return Response({"detail": "Verification email sent."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        try:
            user = User.objects.get(email=email, verification_code=code)
            user.is_active = True  # Activate the user
            user.verification_code = ''  # Clear the verification code
            user.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "detail": "Email verified successfully.",
                "access": str(refresh.access_token),
                "id": user.id
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "Invalid verification code or email."}, status=status.HTTP_400_BAD_REQUEST)


class EmailPasswordLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                if not user.is_active:
                    return Response({"detail": "Account is not verified."}, status=status.HTTP_403_FORBIDDEN)

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'id': user.id,
                }, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid password."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "An unknown error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PasswordResetRequestView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            reset_code = get_random_string(length=5, allowed_chars='0123456789')
            user.verification_code = reset_code
            user.save()

            # Send reset code via email
            send_mail(
                subject='Password Reset Code',
                message=f'Your password reset code is: {reset_code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return Response({"detail": "Password reset code sent to email."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        reset_code = request.data.get('code')
        new_password = request.data.get('new_password')

        try:
            user = User.objects.get(email=email, verification_code=reset_code)
            user.set_password(new_password)
            user.verification_code = ''  # Clear the reset code
            user.save()
            return Response({"detail": "Password reset successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "Invalid reset code or email."}, status=status.HTTP_400_BAD_REQUEST)
