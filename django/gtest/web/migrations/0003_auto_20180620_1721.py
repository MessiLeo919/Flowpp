# Generated by Django 2.0.6 on 2018-06-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180620_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]
