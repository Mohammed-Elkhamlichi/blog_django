from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Article, Category, WebsiteInfo
from .serializers import ArticleSerializer
from django.db.models import Q
from rest_framework.decorators import api_view


# Create your views here.
# Favorate Article
@api_view(("GET",))
def favorate_article(request, article_id):
    article = Article.objects.get(id=article_id)
    articleSerializer = ArticleSerializer(article, many=False)
    if request.GET["query"] == "like":
        user = article.likes.get(id=request.user.id)
        article.likes.get(id=request.user.id).delete()
        article.save()
        print("article like user id", user)
    elif request.GET["query"] == "unlike":
        print("article unlike user id")

    print(request.GET["query"])
    return Response(data={"dev": "Mohammed", "article": articleSerializer.data})


# The Home Page
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
    return render(request, "about.html", {"website": website})


def favorited_articles(request):
    articles = Article.objects.all()
    articles_list = []
    for article in articles:
        if request.user in article.likes.all():
            articles_list.append(article)

    return render(request, "articles/favorited_articles.html", {"articles": articles_list})
