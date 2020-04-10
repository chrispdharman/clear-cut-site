# Generated by Django 3.0.4 on 2020-04-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clear_cut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clearcutconfig',
            name='hyperparameter_one',
        ),
        migrations.AddField(
            model_name='clearcutconfig',
            name='image_size_threshold',
            field=models.IntegerField(default=600),
        ),
        migrations.AddField(
            model_name='clearcutconfig',
            name='noisy_pixel_tolerance',
            field=models.IntegerField(default=4),
        ),
    ]
