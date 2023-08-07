from django.urls import path
from .views import (
    user_login,
)

app_name = "user_app"


urlpatterns = [
    # post views
    path("login/", user_login, name="login"),
]
