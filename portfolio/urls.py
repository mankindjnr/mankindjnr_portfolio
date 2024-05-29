from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resume", views.resume, name="resume"),
    path("new_resume", views.new_resume, name="new_resume"),
    path("download_resume", views.download_resume, name="download_resume"),
]
