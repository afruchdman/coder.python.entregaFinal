# Generated by Django 4.1.5 on 2023-01-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0011_alter_blogs_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='cuerpo',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
