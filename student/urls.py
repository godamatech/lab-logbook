from . import views
from django.urls import path

app_name = "student"
urlpatterns = [
    path("", views.index_view, name="index-view"),
    path("create/", views.create_view, name="create-view"),
]
