# Generated by Django 5.1.6 on 2025-05-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("progres", "0003_alter_progresutilisateur_niveau"),
    ]

    operations = [
        migrations.AlterField(
            model_name="progresutilisateur",
            name="niveau",
            field=models.IntegerField(default=0),
        ),
    ]
