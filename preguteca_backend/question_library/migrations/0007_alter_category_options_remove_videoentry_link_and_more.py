# Generated by Django 4.1.7 on 2023-03-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0006_category_full_name_alter_category_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.RemoveField(
            model_name="videoentry",
            name="link",
        ),
        migrations.AddField(
            model_name="videoentry",
            name="url",
            field=models.CharField(default="", max_length=80, verbose_name="video url"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="category",
            name="full_name",
            field=models.CharField(max_length=50, verbose_name="full name"),
        ),
    ]
