# Generated by Django 3.1.1 on 2020-09-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
