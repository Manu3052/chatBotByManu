# Generated by Django 5.1.3 on 2024-11-24 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0003_remove_message_updated_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="chat",
            new_name="chat_id",
        ),
    ]
