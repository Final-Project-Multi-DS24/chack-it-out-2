# Generated by Django 4.2.3 on 2023-07-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_title",
            field=models.CharField(max_length=100, verbose_name="도서명"),
        ),
    ]
