# Generated by Django 4.1.7 on 2023-03-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0003_alter_videoentry_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.CharField(
                default="unknown", max_length=50, verbose_name="author"
            ),
        ),
    ]
