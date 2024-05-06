from django.urls import include, path
from rest_framework.routers import DefaultRouter

from news.views import (
    home,
    news_details,
    categories_form,
    create_news_form,
    CategoryViewSet,
    UserViewSet,
    NewsViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)
router.register(r"news", NewsViewSet)

urlpatterns = [
    path("", home, name="home-page"),
    path("api/", include(router.urls)),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", categories_form, name="categories-form"),
    path("news/", create_news_form, name="news-form"),
]
