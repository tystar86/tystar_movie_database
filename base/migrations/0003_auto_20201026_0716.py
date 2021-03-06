# Generated by Django 3.1.2 on 2020-10-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_auto_20201026_0713"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="countries",
            field=models.ManyToManyField(blank=True, to="base.Country"),
        ),
        migrations.AlterField(
            model_name="director",
            name="countries",
            field=models.ManyToManyField(blank=True, to="base.Country"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(blank=True, to="base.Actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="categories",
            field=models.ManyToManyField(blank=True, to="base.Category"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="countries",
            field=models.ManyToManyField(blank=True, to="base.Country"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(blank=True, to="base.Director"),
        ),
    ]
