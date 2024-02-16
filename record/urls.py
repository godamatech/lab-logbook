from . import views
from django.urls import path

app_name = "record"
urlpatterns = [
    path("", views.index_view, name="index-view"),
]
