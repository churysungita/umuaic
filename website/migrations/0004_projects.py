# Generated by Django 4.0.2 on 2022-05-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_add_gallery_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='PROJECTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
