from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, "articles/articles.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/article_detail.html", {"article": article})


def categories(request):
    category_list = Category.objects.all()
    return render(request, "articles/categories.html", {"categories": category_list})
