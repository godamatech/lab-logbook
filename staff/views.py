from . import models
from student.models import Record
from django.shortcuts import render


def index_view(request):
    records = Record.objects.all()
    students = models.User.objects.filter(groups__name="student")

    context = {"records": records, "students": students}
    return render(request, "staff/index.html", context)


def detail_view(request, id):
    return render(request, "staff/detail.html")
