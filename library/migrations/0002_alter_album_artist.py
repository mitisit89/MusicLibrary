# Generated by Django 4.1.6 on 2023-02-07 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="artists",
                to="library.artist",
            ),
        ),
    ]
