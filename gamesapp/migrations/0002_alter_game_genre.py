# Generated by Django 5.2.1 on 2025-05-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamesapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="genre",
            field=models.CharField(max_length=150),
        ),
    ]
