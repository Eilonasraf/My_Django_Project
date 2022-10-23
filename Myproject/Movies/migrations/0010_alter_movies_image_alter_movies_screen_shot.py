# Generated by Django 4.0.4 on 2022-05-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0009_alter_movies_image_alter_movies_screen_shot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='screen_shot',
            field=models.ImageField(blank=True, upload_to='screenshots'),
        ),
    ]