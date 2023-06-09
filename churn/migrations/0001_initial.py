# Generated by Django 4.1.7 on 2023-02-15 09:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Back",
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
            ],
            options={
                "verbose_name": "back",
                "verbose_name_plural": "back",
            },
        ),
        migrations.CreateModel(
            name="Data",
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
                (
                    "gender",
                    models.PositiveIntegerField(
                        choices=[(1, "Male"), (0, "Female")], null=True
                    ),
                ),
                (
                    "tenure",
                    models.PositiveIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(72),
                        ],
                    ),
                ),
                (
                    "seniorCitizen",
                    models.PositiveIntegerField(
                        choices=[(1, "Yes"), (0, "No")], null=True
                    ),
                ),
                (
                    "partner",
                    models.PositiveIntegerField(
                        choices=[(1, "Yes"), (0, "No")], null=True
                    ),
                ),
                (
                    "dependents",
                    models.PositiveIntegerField(
                        choices=[(1, "Yes"), (0, "No")], null=True
                    ),
                ),
                (
                    "phone_service",
                    models.PositiveIntegerField(
                        choices=[(1, "Yes"), (0, "No")], null=True
                    ),
                ),
                (
                    "internet_service",
                    models.PositiveIntegerField(
                        choices=[(1, "Yes"), (0, "No")], null=True
                    ),
                ),
                (
                    "charges",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=6,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(8000),
                        ],
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("Electronic check", "Electronic check"),
                            ("Mailed check", "Mailed check"),
                            ("Bank transfer (automatic)", "Bank transfer (automatic)"),
                            ("Credit card (automatic)", "Credit card (automatic)"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
                ("predictions", models.CharField(blank=True, max_length=20)),
            ],
            options={
                "verbose_name": "data",
                "verbose_name_plural": "data",
            },
        ),
        migrations.CreateModel(
            name="Kaki",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
    ]
