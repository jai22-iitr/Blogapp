# Generated by Django 3.2 on 2021-05-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
