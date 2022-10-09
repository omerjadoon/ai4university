
from django.urls import path
from .views import login_view, register_user, student_login_view, student_register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('user/login/', student_login_view, name="loginuser"),
    path('user/register/', student_register_user, name="registeruser"),
    path("user/logout/", LogoutView.as_view(), name="logoutuser")
]
