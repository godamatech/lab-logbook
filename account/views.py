from . import forms
from django.contrib import auth, messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


def logout_view(request):
    auth.logout(request)
    return redirect("/")


def login_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user:
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials")
        return redirect("account:login-view")

    return render(request, "account/login.html")


def register_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            if role:
                group, _ = Group.objects.get_or_create(name=role)
                user.groups.add(group)

            return redirect("account:login-view")

        request.session['form_data'] = form.data
        for key, value in form.errors.items():
            messages.error(request, f"{key}: {value}")
            return redirect("account:register-view")
    return render(request, "account/register.html")
