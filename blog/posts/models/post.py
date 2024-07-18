from django.db import models
from django.contrib.auth.models import User

from blog.posts.models.abc import AbstractPost


class Post(AbstractPost):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=100,
        unique=True,
    )
    body = models.TextField()
    draft = models.BooleanField(default=True)

    class Meta:
        db_table = "posts"
