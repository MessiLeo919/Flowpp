# Generated by Django 2.0.6 on 2018-06-21 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20180621_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='user_name',
            field=models.CharField(editable=False, max_length=30, null=True, verbose_name='用户名'),
        ),
    ]
