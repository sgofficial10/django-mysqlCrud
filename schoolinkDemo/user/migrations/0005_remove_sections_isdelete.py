# Generated by Django 2.2.6 on 2019-10-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191029_0516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sections',
            name='isDelete',
        ),
    ]