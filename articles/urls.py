from django.urls import path
from .views import articles

app_name = "articles"

urlpatterns = [path("articles/", articles, name="articles")]
