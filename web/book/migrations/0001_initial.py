# Generated by Django 3.2.19 on 2023-07-21 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, unique=True, verbose_name='카테고리명')),
            ],
            options={
                'db_table': 'tb_category',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_isbn', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ISBN')),
                ('book_title', models.CharField(max_length=500, verbose_name='도서명')),
                ('book_author', models.CharField(max_length=500, verbose_name='저자')),
                ('book_description', models.CharField(max_length=1000, verbose_name='책소개')),
                ('book_cover', models.CharField(max_length=400, verbose_name='책표지')),
                ('book_publishdate', models.DateField(verbose_name='출간일')),
                ('book_page', models.IntegerField(verbose_name='페이지 수')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category', verbose_name='카테고리')),
            ],
            options={
                'db_table': 'tb_book',
            },
        ),
    ]