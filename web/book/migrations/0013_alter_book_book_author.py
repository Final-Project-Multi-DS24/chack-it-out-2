# Generated by Django 3.2.19 on 2023-07-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_remove_book_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=500, verbose_name='저자'),
        ),
    ]
