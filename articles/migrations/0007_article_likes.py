# Generated by Django 4.1.7 on 2023-03-10 22:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0006_alter_websiteinfo_about_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="post_likes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
