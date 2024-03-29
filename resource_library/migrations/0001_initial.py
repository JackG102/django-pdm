# Generated by Django 5.0.1 on 2024-01-08 00:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('author', models.CharField(max_length=200)),
                ('body', ckeditor.fields.RichTextField()),
                ('type', models.CharField(choices=[('pdf', 'PDF'), ('video', 'Video'), ('podcast', 'Podcast'), ('website', 'Website'), ('book', 'Book')], max_length=50)),
                ('pub_date', models.DateField(verbose_name='date published')),
            ],
        ),
    ]
