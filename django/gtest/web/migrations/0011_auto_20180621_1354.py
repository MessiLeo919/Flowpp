# Generated by Django 2.0.6 on 2018-06-21 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20180621_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
