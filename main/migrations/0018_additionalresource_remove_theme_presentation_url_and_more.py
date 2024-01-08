# Generated by Django 4.2.6 on 2024-01-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_alter_theme_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdditionalResource",
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
                ("url", models.URLField()),
                ("title", models.CharField(verbose_name=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="theme",
            name="presentation_url",
        ),
        migrations.AddField(
            model_name="theme",
            name="additional_resources",
            field=models.ManyToManyField(to="main.additionalresource"),
        ),
    ]