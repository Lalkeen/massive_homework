from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import DetailView

from .forms import UserRegistrationForm, LoginForm, UserEditForm, BaseUserEditForm
from .models import BaseUser


@login_required
def dashboard(request):
    return render(request, "user_app/dashboard.html", {"section": "dashboard"})


# @login_required
class UserDetailView(DetailView):
    model = User


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
            return render(
                request,
                "user_app/dashboard.html",
            )
    else:
        user_form = UserEditForm(instance=request.user)
        base_edit_form = BaseUserEditForm(instance=request.user.baseuser)
        return render(
            request,
            "user_app/edit.html",
            {"user_form": user_form, "base_user_form": base_edit_form},
        )


def edit_user(request, pk, **kwargs):
    if request.method == "POST":
        user_data = User.objects.get(pk=pk)
        user_form = UserEditForm(instance=user_data, data=request.POST)
        base_edit_form = BaseUserEditForm(
            instance=BaseUser.objects.get(user_id=user_data.pk),
            data=request.POST,
            files=request.FILES,
        )
        if user_form.is_valid() and base_edit_form.is_valid():
            user_form.save()
            base_edit_form.save()
            return HttpResponseRedirect(
                reverse(
                    "user_app:userprofile",
                    kwargs={"pk": user_data.pk},
                )  # pk=user_data.pk)
            )
    else:
        user_data = User.objects.get(pk=pk)
        user_form = UserEditForm(instance=user_data)
        base_edit_form = BaseUserEditForm(instance=user_data.baseuser)
        return render(
            request,
            "user_app/edit_user.html",
            {
                "user_form": user_form,
                "base_user_form": base_edit_form,
                "user": user_data,
            },
        )
