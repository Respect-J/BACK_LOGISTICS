from django.urls import path
from .views import (
    UserRegistrationView,
    VerifyEmailView,
    EmailPasswordLoginView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('login/', EmailPasswordLoginView.as_view(), name='email-login'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
