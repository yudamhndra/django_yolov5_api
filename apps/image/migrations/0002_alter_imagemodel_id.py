# Generated by Django 4.2.6 on 2023-10-19 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagemodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
