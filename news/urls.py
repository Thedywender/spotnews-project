from django.urls import path
from news.views import home, news_details, categories_form, create_news_form

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", create_news_form, name="news-form"),
]
