# Generated by Django 4.1.7 on 2023-04-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Livre',
        ),
        migrations.RenameField(
            model_name='livre',
            old_name='title',
            new_name='titre',
        ),
    ]
