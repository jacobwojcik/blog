# Generated by Django 3.1.1 on 2020-09-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_auto_20200907_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=models.TextField(max_length=5000),
        ),
    ]
