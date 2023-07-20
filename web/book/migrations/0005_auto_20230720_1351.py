# Generated by Django 3.2.19 on 2023-07-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_id_alter_book_book_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_page',
        ),
        migrations.AddField(
            model_name='book',
            name='book_publishdate',
            field=models.DateField(default='2023-01-01', verbose_name='출간일'),
            preserve_default=False,
        ),
    ]
