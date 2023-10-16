# Generated by Django 4.1.7 on 2023-10-16 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "question_library",
            "0033_homepageinformationcard_alter_homepage_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="information_cards",
            field=models.ManyToManyField(to="question_library.homepageinformationcard"),
        ),
        migrations.AlterField(
            model_name="videoentry",
            name="yt_publish_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 10, 16, 15, 51, 28, 341074),
                verbose_name="Youtube - Video publication date",
            ),
        ),
    ]
