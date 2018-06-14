from django.contrib.auth import (
    authenticate,
    login,
)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserRegisterForm


def register_view(request):
    title = "ثبت نام"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return HttpResponseRedirect(reverse("siteinfo:groups",  kwargs={}))

    context = {
        "form": form,
        "title": title
    }
    return render(request, "users/form.html", context)
# Create your views here.
