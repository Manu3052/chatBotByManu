# Generated by Django 5.1.3 on 2024-11-23 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0004_alter_chat_contact_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chat",
            old_name="chat_id",
            new_name="chat",
        ),
    ]