from django import forms
from django.forms import (
    CheckboxSelectMultiple,
    ModelForm,
    TextInput,
    Textarea,
    DateInput,
    FileInput,
    ModelChoiceField,
    ModelMultipleChoiceField,
)

from .models import News, Category, User


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={
                    "maxlength": "200",
                    "required": True,
                    "id": "id_name",
                    "class": "categories-fieldset",
                }
            ),
        }
        labels = {
            "name": "Nome",
        }


class NewsForm(ModelForm):
    author = ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"id": "id_author"}),
    )
    categories = ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"id": "id_categories"}),
    )

    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            "title": TextInput(
                attrs={
                    "maxlength": "200",
                    "required": True,
                    "id": "id_title",
                }
            ),
            "content": Textarea(attrs={"required": True, "id": "id_content"}),
            "created_at": DateInput(
                attrs={"required": True, "type": "date", "id": "id_created_at"}
            ),
            "image": FileInput({"id": "id_image"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["created_at"].label = "Criado em"
        self.fields["image"].label = "URL da Imagem"
        self.fields["categories"].label = "Categorias"


# class NewsForm(ModelForm):
#     author = ModelChoiceField(queryset=User.objects.all())
#     categories = ModelMultipleChoiceField(
#         queryset=Category.objects.all(), widget=CheckboxSelectMultiple
#     )

#     class Meta:
#         model = News
#         fields = "__all__"
#         widgets = {
#             "title": TextInput(attrs={"maxlength": "200", "required": True}),
#             "content": Textarea(attrs={"required": True}),
#             "created_at": DateInput(attrs={"required": True, "type": "date"}),
#             "image": FileInput(),
#         }
#         labels = {
#             "title": "Título",
#             "content": "Conteúdo",
#             "author": "Autoria",
#             "created_at": "Criado em",
#             "image": "URL da Imagem",
#             "categories": "Categorias",
#         }
