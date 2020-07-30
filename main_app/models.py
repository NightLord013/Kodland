from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length = 80, verbose_name = "Заголовок")
    text = models.TextField(verbose_name = "Текст")
    photo = models.ImageField(upload_to = 'images/', verbose_name = "Фото")
    pubdate = models.DateTimeField(auto_now = True, verbose_name = "Дата публикации")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', '-pubdate']
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        
