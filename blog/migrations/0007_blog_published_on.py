# Generated by Django 3.2 on 2021-04-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210430_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
