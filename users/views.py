from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

from django.shortcuts import render, redirect

from users.models import ContactInfo
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login_view(request):
    next = request.GET.get('next')
    # title = "Login"
    title = "ورود"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "default_form.html", {"form":form, "title": title})


def register_view(request):
    next = request.GET.get('next')
    title = "ثبت نام"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }
    return render(request, "default_form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

def edit_profile(request):
    instance = None
    if request.user.is_authenticated:
        instance = request.user.profile
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        tg = ContactInfo.objects.filter(user = instance)
        if tg.exists():
            tg = tg.first()
        else:
            tg = ContactInfo()
            tg.user = instance
        tg.info = form.cleaned_data.get('telegram_id')
        tg.save()
        messages.success(request, "فرم با موفقیت ثبت شد", extra_tags='html_safe')
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "default_restricted_form.html", context)