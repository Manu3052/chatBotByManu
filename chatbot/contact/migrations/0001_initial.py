# Generated by Django 5.1.3 on 2024-11-21 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("cpf", models.CharField(blank=True, max_length=11, null=True)),
                ("telephone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
