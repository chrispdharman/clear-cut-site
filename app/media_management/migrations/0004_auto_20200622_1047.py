# Generated by Django 3.0.4 on 2020-06-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_management', '0003_auto_20200622_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaitem',
            name='description',
            field=models.TextField(max_length=1048, null=True),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='label',
            field=models.TextField(max_length=128, null=True),
        ),
    ]
