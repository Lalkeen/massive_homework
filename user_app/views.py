from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserRegistrationForm


@login_required
def dashboard(request):
    return render(request, "user_app/dashboard.html", {"section": "dashboard"})


#
# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd["username"], password=cd["password"])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse("user_app:dashboard"))
#                 else:
#                     return HttpResponse("Disabled account")
#             else:
#                 return HttpResponse("Invalid login")
#     else:
#         form = LoginForm()
#     return render(request, "user_app/login.html", {"form": form})
#

# def password_reset_done(request):
#     return render(request, "user_app/password_reset_done.html)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # Save the User object
            new_user.save()
            return render(
                request, "user_app/register_done.html", {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "user_app/register.html", {"user_form": user_form})
