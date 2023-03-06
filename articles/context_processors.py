from .models import Article


def latest_articles(request):
    return {"last_articles": Article.objects.order_by('-create_at')[:3]}
