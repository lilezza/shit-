# Generated by Django 5.1.1 on 2024-10-19 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articles_options_alter_articles_body_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'permissions': (('private_section_article', 'Private Section Article'),), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
    ]
