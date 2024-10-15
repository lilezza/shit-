# Generated by Django 5.1.1 on 2024-10-13 17:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_show'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='show',
            field=models.BooleanField(default=1, verbose_name='نمایش'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='view',
            field=models.IntegerField(default=0, verbose_name='بازدید ها'),
        ),
    ]
