# Generated by Django 2.2.5 on 2019-09-08 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("recipesapp", "0002_auto_20190908_0122")]

    operations = [
        migrations.AddField(
            model_name="recipeingredient",
            name="cost",
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        )
    ]