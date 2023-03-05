from django.urls import path
from .views import home, article_detail, categories, category_detail

app_name = "articles"

urlpatterns = [
    path("", home, name="home"),
    path("articles/<int:article_id>/detail/", article_detail, name="article_detail"),
    path("categories/list/", categories, name="categories"),
    path("categories/<int:category_id>/detail/", category_detail, name="category_detail"),
]
