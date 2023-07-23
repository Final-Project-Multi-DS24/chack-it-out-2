# Generated by Django 3.2.19 on 2023-07-23 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=2000, verbose_name='리뷰')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book', verbose_name='도서')),
            ],
            options={
                'db_table': 'tb_reviewUser',
            },
        ),
    ]