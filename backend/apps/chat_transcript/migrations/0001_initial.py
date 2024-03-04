# Generated by Django 4.2.1 on 2024-02-29 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("chat_history", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatTranscript",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("message", models.TextField()),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("system", "SYSTEM"),
                            ("user", "USER"),
                            ("assistant", "ASSISTANT"),
                            ("function", "FUNCTION"),
                            ("tool", "TOOL"),
                        ],
                        db_comment="Role of the messenger.",
                        editable=False,
                    ),
                ),
                (
                    "chat_history",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_history_transcript",
                        to="chat_history.chathistory",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="transcript_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="transcript_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_message",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="chat_transcript.chattranscript",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]