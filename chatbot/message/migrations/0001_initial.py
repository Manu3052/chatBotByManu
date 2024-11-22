# Generated by Django 5.1.3 on 2024-11-22 05:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("chat", "0003_chat_chat_id_alter_chat_service_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                    "sender_type",
                    models.IntegerField(
                        choices=[(1, "User"), (2, "Bot"), (3, "Support Agent")],
                        default=1,
                        help_text="The type of sender for the message (1 = USER, 2 = BOT, 3 = SUPPORT_AGENT).",
                    ),
                ),
                (
                    "message_content",
                    models.TextField(
                        help_text="The content of the message (cannot be null)."
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Timestamp when the message was last updated (optional).",
                        null=True,
                    ),
                ),
                (
                    "chat",
                    models.ForeignKey(
                        help_text="The chat to which this message belongs.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="chat.chat",
                    ),
                ),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
                "ordering": ["created_at"],
            },
        ),
    ]