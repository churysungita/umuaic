# Generated by Django 4.0.2 on 2022-05-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('kiasi_kilichopatikana', models.CharField(max_length=20)),
                ('kiasi_kinachohitajika', models.CharField(max_length=20)),
            ],
        ),
    ]
