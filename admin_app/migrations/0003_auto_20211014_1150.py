# Generated by Django 3.2.3 on 2021-10-14 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_auto_20211014_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
