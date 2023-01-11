# Generated by Django 4.1.5 on 2023-01-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=1024, null=True)),
                ('emisor', models.CharField(max_length=256)),
                ('receptor', models.CharField(max_length=256, null=True)),
                ('leido', models.BooleanField(default=False)),
            ],
        ),
    ]
