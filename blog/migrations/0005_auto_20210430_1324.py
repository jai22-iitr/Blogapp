# Generated by Django 3.2 on 2021-04-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='edited_on',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='published_on',
        ),
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.IntegerField(default='30'),
        ),
        migrations.AddField(
            model_name='blog',
            name='month',
            field=models.CharField(default='', max_length=3),
        ),
    ]
