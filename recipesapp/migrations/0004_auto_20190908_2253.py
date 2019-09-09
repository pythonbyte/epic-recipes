# Generated by Django 2.2.5 on 2019-09-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0003_recipeingredient_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='ingredients',
            new_name='ingredient',
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
