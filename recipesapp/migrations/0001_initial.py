# Generated by Django 2.2.5 on 2019-09-08 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("ingredientsapp", "0002_auto_20190907_2301")]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("preparation_time", models.PositiveIntegerField()),
                ("ingredients", models.ManyToManyField(to="ingredientsapp.Ingredient")),
            ],
        )
    ]