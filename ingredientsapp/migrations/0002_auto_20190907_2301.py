# Generated by Django 2.2.5 on 2019-09-07 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='units',
            new_name='unit',
        ),
    ]
