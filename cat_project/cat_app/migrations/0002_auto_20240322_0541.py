# Generated by Django 2.1.5 on 2024-03-22 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cat',
            new_name='Pet',
        ),
    ]
