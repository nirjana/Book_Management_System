# Generated by Django 4.0.1 on 2022-01-17 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0009_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
    ]