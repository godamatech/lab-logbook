from . import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test


def index_view(request):
    return render(request, "student/index.html")
