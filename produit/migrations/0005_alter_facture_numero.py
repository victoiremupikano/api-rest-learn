# Generated by Django 5.1 on 2024-08-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produit", "0004_alter_client_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="numero",
            field=models.IntegerField(),
        ),
    ]
