# Generated by Django 4.1.5 on 2023-01-10 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0013_uploads'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='uploads',
            new_name='Imagen',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='imagen',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
