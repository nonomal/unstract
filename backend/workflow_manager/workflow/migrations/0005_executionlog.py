# Generated by Django 4.2.1 on 2024-05-23 08:50

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0004_filehistory_workflow_cachekey"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExecutionLog",
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
                (
                    "execution_id",
                    models.UUIDField(db_comment="Execution ID", editable=False),
                ),
                ("data", models.JSONField(db_comment="Execution log data")),
                (
                    "event_time",
                    models.DateTimeField(db_comment="Execution log event time"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
