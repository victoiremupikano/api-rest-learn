# Generated by Django 5.1 on 2024-09-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturation', '0003_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='date_fact',
            field=models.DateField(auto_now_add=True),
        ),
    ]
