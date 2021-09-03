# Generated by Django 3.2.7 on 2021-09-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, max_length=300, unique=True)),
                ('image', models.TextField()),
                ('isbn', models.CharField(max_length=50, unique=True)),
                ('price', models.IntegerField()),
                ('pubdate', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
