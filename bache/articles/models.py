from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100 , verbose_name = 'عنوان')

    class Meta :
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=100 , verbose_name= "عنوان")
    body = models.TextField( verbose_name= "متن")
    view = models.IntegerField(default=0, verbose_name= "بازدید ها")
    show = models.BooleanField(default = 1, verbose_name= "نمایش")
    published_at = models.DateTimeField(default= timezone.now, verbose_name= "زمان انتشار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "زمان ساخت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name= "زمان بروزرسانی")
    user = models.ForeignKey(User, on_delete = models.SET_NULL , null = True)
    #اگه بخوام هم یوزرم پاک بشه هم مقاله هاش می تونم ازmodels.CASCADE استفاده کنم
    categories = models.ManyToManyField(Category , verbose_name = "دسته بندی ها")

    class Meta :
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        permissions = (
            ('private_section_article','Private Section Article'),
        )

    def __str__(self):
        return self.title


class Aextra(models.Model):
    sticky = models.BooleanField(verbose_name = "سنجاق" , default = False)
    tags = models.CharField(max_length = 100 , verbose_name = "تگ")

    article = models.OneToOneField(Articles , on_delete = models.CASCADE , primary_key = True)

    class Meta :
        verbose_name = "فیلد ویژه"
        verbose_name_plural = "فیلد های ویژه"

    def __str__(self):
        return self.article.title
