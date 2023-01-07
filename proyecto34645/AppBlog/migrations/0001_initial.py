# Generated by Django 4.1.3 on 2023-01-06 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=256)),
                ('cuerpo', models.CharField(max_length=1024)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.TimeField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=256)),
            ],
        ),
    ]