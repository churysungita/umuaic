# Generated by Django 4.0.2 on 2022-05-23 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_gallery_add_gallery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_gallery',
            new_name='gallery',
        ),
    ]
