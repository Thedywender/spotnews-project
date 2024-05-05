from django.forms import ModelForm
from news.models import Category, News


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"
