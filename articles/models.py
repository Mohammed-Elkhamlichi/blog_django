from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="media/categories/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Article(models.Model):
    likes = models.ManyToManyField(User, blank=True, null=True, related_name="post_likes")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/articles", blank=True, null=True)
    content = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class WebsiteInfo(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    about = RichTextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
