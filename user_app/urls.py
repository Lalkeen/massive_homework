from django.urls import path, include
from .views import (
    register,
    user_login,
    edit,
    dashboard,
)

app_name = "user_app"


urlpatterns = [
    # post views
    path("dashboard/", dashboard, name="dashboard"),
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("edit/", edit, name="edit"),
]
