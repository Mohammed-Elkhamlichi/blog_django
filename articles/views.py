from django.shortcuts import render, get_object_or_404
from .models import Article, Category, WebsiteInfo
from django.db.models import Q


# Create your views here.
def home(request):
    search = request.GET["search"] if request.GET else None
    print("search", search)
    articles = (
        Article.objects.filter(Q(title__contains=search) | Q(content__contains=search))
        if search is not None
        else Article.objects.all()
    )
    # articles =
    return render(request, "articles/articles.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/article_detail.html", {"article": article})


def categories(request):
    category_list = Category.objects.all()
    return render(request, "articles/categories.html", {"categories": category_list})


def category_detail(request, category_id):
    articles = Article.objects.filter(category=category_id)
    return render(request, "articles/category_detail.html", {"articles": articles})


def about(request):
    website = WebsiteInfo.objects.all().first()
    return render(request, "about.html", {"website":website})
