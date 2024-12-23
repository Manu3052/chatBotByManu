# Generated by Django 5.1.3 on 2024-11-22 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_chat_chat_id_alter_chat_service_and_more"),
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="contact_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact_chats",
                to="contact.contact",
            ),
        ),
    ]
