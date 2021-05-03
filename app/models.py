# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Post(models.Model):
    h1 = models.CharField(max_length=200, verbose_name='Заголовок')
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField()
    description = RichTextUploadingField(verbose_name="Описание")
    content = RichTextUploadingField(verbose_name='Контент статьи')
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now, verbose_name='Время создания статьи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи')
    tags = TaggableManager(verbose_name="Тег")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
