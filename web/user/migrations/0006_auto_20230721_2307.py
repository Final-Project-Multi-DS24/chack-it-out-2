# Generated by Django 3.2.19 on 2023-07-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, verbose_name='이름'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='tb_user',
        ),
    ]
