# Generated by Django 4.2.6 on 2023-12-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_alter_userprofile_address_alter_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stories',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
