# Generated by Django 4.0.4 on 2022-05-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0006_alter_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(null=True, upload_to='assets/'),
        ),
    ]
