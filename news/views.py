from django.shortcuts import render
from news.models import News


def home(request):
    context = News.objects.all()
    return render(request, "home.html", {"news": context})


def news_details(request, id):
    context = News.objects.get(id=id)
    return render(request, "news_details.html", {"news_details": context})


# def categories_form(request):
#     if request.method == "POST":
#         category = CategoryForm(request.POST)
#         if category.is_valid():
#             category.save()
#             request.session["category_id"] = category.instance.id
#             return redirect("home-page")
#     elif request.method == "GET":
#         return render(
#             request, "news_details.html", {"category_form": CategoryForm()}
#         )


# O template do formulário de uma nova categoria deve ter uma tag de formulário com a propriedade method do tipo post e a propriedade action com a url para /categories;
# O template do formulário de uma nova categoria deve carregar o token de segurança CSRF em seu interior usando a tag de template adequada;
# O template do formulário de uma nova categoria deve ter uma label que como o valor Nome;
# O template do formulário de uma nova categoria deve ter um input com as algumas especificações:
# A propriedade type do tipo text;
# A propriedade name com o valor name;
# A propriedade maxlength com o valor 200;
# Precisa ser um campo obrigatório;
# O template do formulário de uma nova categoria deve ter um botão do tipo submit com texto Salvar;
# Após o cadastro de uma categoria, a pessoa usuária deve ser redirecionada para a página principal;
