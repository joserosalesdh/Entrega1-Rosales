# Generated by Django 4.0.4 on 2022-05-03 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='fechaPublicacion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fechaPublicacion',
        ),
    ]
