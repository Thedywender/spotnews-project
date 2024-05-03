from django.shortcuts import render
from news.models import News


def home(request):
    context = News.objects.all()
    return render(request, "home.html", {"news": context})
