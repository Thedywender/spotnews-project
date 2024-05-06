from django.shortcuts import render, redirect
from news.models import News, Category, User
from news.forms import CategoryForm, NewsForm
from rest_framework import viewsets

from news.serializers import CategorySerializer, UserSerializer


def home(request):
    context = News.objects.all()
    return render(request, "home.html", {"news": context})


def news_details(request, id):
    context = News.objects.get(id=id)
    return render(request, "news_details.html", {"news_details": context})


def categories_form(request):
    if request.method == "POST":
        category = CategoryForm(request.POST)
        if category.is_valid():
            Category.objects.create(**category.cleaned_data)
            return redirect("home-page")
    else:
        category = CategoryForm()
    return render(request, "categories_form.html", {"form": category})


def create_news_form(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        categories = form.cleaned_data.pop("categories")
        news_instance = form.save()
        news_instance.categories.set(categories)
        return redirect("home-page")
    return render(
        request,
        "news_form.html",
        {
            "form_news": form,
            "categories": Category.objects.all(),
            "users": User.objects.all(),
        },
    )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
