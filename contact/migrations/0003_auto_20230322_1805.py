# Generated by Django 3.1.14 on 2023-03-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20230322_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.CharField(max_length=2000),
        ),
    ]
