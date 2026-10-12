from django.db import models
from django.conf import settings
from django.urls import reverse

class Article (models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    body = models.TextField(verbose_name="محتوا")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    verbose_name="نویسنده"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])

