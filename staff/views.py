from . import models
from django.shortcuts import render


def index_view(request):
    return render(request, "staff/index.html")

def detail_view(request, id):
    return render(request, "staff/detail.html")
