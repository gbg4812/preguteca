# Generated by Django 4.2.10 on 2024-03-13 22:05

from django.db import migrations


def migrate_posts(apps, schema_editor):
    Post = apps.get_model("question_library", "Post")
    VideoPost = apps.get_model("question_library", "VideoPost")
    TextPost = apps.get_model("question_library", "TextPost")

    def exclude_keys(d: dict[str, any], keys: list[str]) -> dict[str, any]:
        return {key: d[key] for key in d if key not in keys}

    for tp_val in TextPost.objects.all().values():
        Post.objects.update_or_create(**exclude_keys(tp_val, ["id"]))
    for vp_val in VideoPost.objects.all().values():
        Post.objects.update_or_create(**exclude_keys(vp_val, ["id"]))


class Migration(migrations.Migration):
    dependencies = [
        ("question_library", "0060_alter_post_content"),
    ]

    operations = [migrations.RunPython(migrate_posts, migrations.RunPython.noop)]