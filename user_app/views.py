from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import UserRegistrationForm, LoginForm, UserEditForm, BaseUserEditForm
from .models import BaseUser


@login_required
def dashboard(request):
    return render(request, "user_app/dashboard.html", {"section": "dashboard"})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("user_app:dashboard"))
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "user_app/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            base_user = BaseUser.objects.create(user=new_user)
            return render(
                request, "user_app/register_done.html", {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "user_app/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        base_edit_form = BaseUserEditForm(
            instance=request.user.baseuser, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and base_edit_form.is_valid():
            user_form.save()
            base_edit_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        base_edit_form = BaseUserEditForm(instance=request.user.baseuser)
        return render(
            request,
            "user_app/edit.html",
            {"user_form": user_form, "base_user_form": base_edit_form},
        )
