# Generated by Django 5.1 on 2024-08-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produit", "0006_alter_facture_numero"),
    ]

    operations = [
        migrations.AddField(
            model_name="produit",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="Images/Produit"),
        ),
    ]
