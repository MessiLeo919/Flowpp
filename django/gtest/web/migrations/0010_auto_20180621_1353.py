# Generated by Django 2.0.6 on 2018-06-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20180621_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='user_name',
            field=models.CharField(default='', max_length=30, verbose_name='用户名'),
        ),
    ]
