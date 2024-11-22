# Generated by Django 5.1.3 on 2024-11-22 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_alter_chat_start_time"),
        ("supportAgent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="chat_id",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="chat",
            name="service",
            field=models.CharField(
                choices=[("0", "Telegram"), ("1", "Discord")], max_length=2
            ),
        ),
        migrations.AlterField(
            model_name="chat",
            name="support_agent_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="support_chats",
                to="supportAgent.supportagent",
            ),
        ),
    ]