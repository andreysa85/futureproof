from django.db import models
from django.utils.timezone import now
# Create your models here.


class Post (models.Model):
    post_name = models.CharField(verbose_name='Название поста', max_length=30)
    post = models.TextField(verbose_name='Пост')
    author = models.CharField(verbose_name='Автор', max_length=30)
    time_creation = models.DateTimeField(verbose_name='Время создания',default=now, editable=True)
    time_publication = models.DateTimeField(verbose_name='Время публикации', default=now, editable=True)
    time_update = models.DateTimeField(default=now, editable=True)
    image = models.ImageField(upload_to='img/', blank=True, null=True)





