# Generated by Django 4.2.6 on 2024-01-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0025_homework_attachments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homework",
            name="attachments",
        ),
        migrations.DeleteModel(
            name="Attachment",
        ),
        migrations.AddField(
            model_name="homework",
            name="attachments",
            field=models.FileField(default=[], upload_to="uploads/"),
            preserve_default=False,
        ),
    ]
