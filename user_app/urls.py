from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    register,
    # user_login,
    # user_logout,
    # user_logout-login,
    dashboard,
)

app_name = "user_app"


urlpatterns = [
    # post views
    path("dashboard/", dashboard, name="dashboard"),
    # path("login/", auth_views.LoginView.as_view(), name="login")
    path("", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
