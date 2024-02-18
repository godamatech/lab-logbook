from . import models, forms
from django.contrib import messages
from django.utils.timezone import now
from django.shortcuts import render, redirect


def index_view(request):
    total = models.Record.objects.filter(user=request.user)

    others = total.exclude(created_at__date=now().date())
    current = total.filter(user=request.user, created_at__date=now().date()).first()

    context = {"current": current, "others": others, "total": total}
    return render(request, "student/index.html", context)


def create_view(request):
    if request.method == "POST":
        form = forms.RecordForm(request.POST)
        if form.is_valid():
            instance = form.save(False)

            instance.user = request.user
            instance.save()

            return redirect("student:index-view")

        messages.error(request, "Failed to save record")
        return redirect("student:create-view")
    return render(request, "student/create.html")
