from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Post(models.Model):

    name = models.CharField(max_length=100, verbose_name='Заголовок', unique=True)
    slug = models.SlugField(unique=True)
    message = models.TextField(verbose_name='Сообщение')
    image = models.ImageField(upload_to='images/blog/%Y/%m/%d', verbose_name='Изображение', help_text='700px-400px')
    date_create = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания записи')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения записи')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date_create']

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.slug}'

