# Generated by Django 2.2.6 on 2019-10-29 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_sections_isdelete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sections',
            old_name='class_id',
            new_name='classes',
        ),
    ]
