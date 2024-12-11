from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from api.views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register"),
    path('login/',UserLoginView.as_view(),name="login"),
    path('profile/',UserProfileView.as_view(),name="profile"),
    path('changepass/',UserChangePasswordView.as_view(),name="changepass"),
    path('reset/',SendPasswordResetEmailView.as_view(),name="reset"),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name="reset-password")
]
