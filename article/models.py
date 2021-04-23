from django.db import models


class Article(models.Model):
    title = models.CharField('タイトル', max_length=50)
    content = models.TextField('内容', max_length=1000)
    is_publish = models.BooleanField('公開済み', default=True)

    class Meta:
        verbose_name = "記事"
        verbose_name_plural = "記事"
