from django.urls import path, include
from .views import (
    register,
    user_login,
    edit,
    edit_user,
    dashboard,
    UserDetailView,
)

app_name = "user_app"


urlpatterns = [
    # post views
    path("dashboard/", dashboard, name="dashboard"),
    path(
        "<int:pk>/",
        UserDetailView.as_view(template_name="user_app/user_detail.html"),
        name="userprofile",
    ),
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("edit/", edit, name="edit"),
    path("edit/<int:pk>", edit_user, name="edit-user"),
]
