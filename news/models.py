from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


def validate_title(value):
    words = value.split()
    if len(words) <= 1:
        raise ValidationError("O título deve ter mais de uma palavra.")


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_title], blank=False, null=False
    )
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    created_at = models.DateField(blank=False, null=False)
    img = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField(
        Category, related_name="news", blank=False
    )

    def __str__(self) -> str:
        return self.title
