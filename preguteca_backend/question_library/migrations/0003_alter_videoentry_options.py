# Generated by Django 4.1.7 on 2023-03-08 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_library', '0002_alter_category_options_videoentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoentry',
            options={'verbose_name_plural': 'Video entries'},
        ),
    ]
