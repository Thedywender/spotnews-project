from django.shortcuts import render, redirect
from news.models import News, Category
from news.forms import CategoryForm


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
