# Generated by Django 4.1.7 on 2023-10-10 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0028_alter_videoentry_yt_publish_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="description"
            ),
        ),
        migrations.AlterField(
            model_name="videoentry",
            name="yt_publish_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 10, 10, 16, 55, 31, 390919),
                verbose_name="Youtube - Video publication date",
            ),
        ),
    ]