# Generated by Django 4.1.7 on 2023-06-12 20:46

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('question_library', '0014_videotype_videoentry_language_videoentry_youtube_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoentry',
            name='video_url',
            field=models.CharField(blank=True, max_length=200, verbose_name='video url'),
        ),
        migrations.AddField(
            model_name='videoentry',
            name='yt_channel_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Youtube - Channel title'),
        ),
        migrations.AddField(
            model_name='videoentry',
            name='yt_publish_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 12, 22, 46, 50, 323863),
                                       verbose_name='Youtube - Video publication date'),
        ),
        migrations.AlterField(
            model_name='videoentry',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='videoentry',
            name='video_types',
            field=models.ManyToManyField(blank=True, to='question_library.videotype', verbose_name='Video Type'),
        ),
        migrations.AlterField(
            model_name='videoentry',
            name='youtube_id',
            field=models.CharField(blank=True, default='', max_length=16, verbose_name='Youtube video id'),
        ),
    ]
