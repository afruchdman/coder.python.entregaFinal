# Generated by Django 4.1.3 on 2023-01-06 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='veterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pages',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppBlog.blog'),
            preserve_default=False,
        ),
    ]
