# Generated by Django 4.1.6 on 2023-06-19 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("Name", models.CharField(max_length=20, unique=True)),
                ("DOB", models.DateField()),
                ("Email", models.EmailField(max_length=300, unique=True)),
                ("Gender", models.CharField(max_length=100)),
                ("Locality", models.CharField(max_length=100)),
                ("City", models.CharField(max_length=100)),
                ("Pin", models.PositiveIntegerField()),
                (
                    "State",
                    models.CharField(
                        choices=[
                            ("Maharashtra", "Maharatashtra"),
                            ("Bihar", "Bihar"),
                            ("Assam", "Assam"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Tripura", "Tripura"),
                            ("Rajasthan", "Rajasthan"),
                            ("Tamil Nadu", "Tamil Nadu"),
                            ("Uttrakhand", "Uttrakhand"),
                        ],
                        max_length=100,
                    ),
                ),
                ("Resume", models.FileField(upload_to="Emp_Resume")),
                ("Phone", models.PositiveIntegerField(max_length=10)),
                ("Joining_Date", models.DateField(auto_now_add=True)),
                (
                    "Profile_Photo",
                    models.ImageField(blank=True, null=True, upload_to="Emp_Images"),
                ),
            ],
        ),
    ]
