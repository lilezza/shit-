from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=100 , verbose_name= "عنوان")
    body = models.TextField( verbose_name= "متن")
    view = models.IntegerField(default=0, verbose_name= "بازدید ها")
    show = models.BooleanField(default = 1, verbose_name= "نمایش")
    published_at = models.DateTimeField(default= timezone.now, verbose_name= "زمان انتشار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "زمان ساخت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name= "زمان بروزرسانی")

    class Meta :
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
