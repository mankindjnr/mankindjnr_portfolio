from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")


def resume(request):
    return render(request, "portfolio/resume.html")
