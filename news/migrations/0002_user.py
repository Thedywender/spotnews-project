# Generated by Django 4.2.3 on 2024-05-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("role", models.CharField(max_length=200)),
            ],
        ),
    ]
