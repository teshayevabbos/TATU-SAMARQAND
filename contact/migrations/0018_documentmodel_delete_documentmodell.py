# Generated by Django 4.2.1 on 2023-05-31 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_documentmodell_delete_documentmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='pdf')),
                ('types', models.CharField(choices=[('word', '.docx'), ('pdf', '.pdf'), ('excel', '.xlsx'), ('powerpoint', '.pptx')], max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DocumentModell',
        ),
    ]