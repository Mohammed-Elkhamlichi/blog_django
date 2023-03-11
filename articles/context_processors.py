from .models import Article


def latest_articles(request):
    articles = Article.objects.all()
    favorited_articles_list = []
    for article in articles:
        if request.user in article.likes.all():
            favorited_articles_list.append(article)
    return {
        "last_articles": Article.objects.order_by("-create_at")[:4],
        "favorited_articles_list": len(favorited_articles_list),
    }
