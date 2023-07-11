# Generated by Django 4.1.6 on 2023-06-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("Age", models.IntegerField()),
                ("Email", models.EmailField(max_length=300, unique=True)),
                ("Emp_id", models.CharField(max_length=4, unique=True)),
                ("Experience", models.CharField(max_length=20)),
                ("Resume", models.FileField(upload_to="Emp_Resume")),
                ("Salary", models.CharField(max_length=20)),
                ("Position", models.CharField(blank=True, max_length=100, null=True)),
                ("Phone", models.CharField(max_length=10)),
                ("Address", models.TextField(max_length=200)),
                ("Joining_Date", models.DateField(auto_now_add=True)),
                ("Photo", models.ImageField(upload_to="Emp_Images")),
            ],
        ),
    ]