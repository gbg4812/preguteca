# Generated by Django 4.2.10 on 2024-03-13 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('question_library', '0063_alter_homepage_ordered_posts'), ('question_library', '0064_alter_homepage_ordered_posts_and_more'), ('question_library', '0065_rename_ordered_posts_homepage_posts_and_more'), ('question_library', '0066_rename_orderedpost_postwithposition'), ('question_library', '0067_alter_postwithposition_home_page')]

    dependencies = [
        ('question_library', '0062_remove_videopost_video_alter_homepage_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='ordered_posts',
            new_name='posts',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='posts',
            field=models.ManyToManyField(related_name='+', through='question_library.OrderedPost', to='question_library.post'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='posts',
            field=models.ManyToManyField(through='question_library.OrderedPost', to='question_library.post'),
        ),
        migrations.AlterField(
            model_name='orderedpost',
            name='home_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_post_relationship', to='question_library.homepage'),
        ),
        migrations.AlterField(
            model_name='orderedpost',
            name='home_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_posts', to='question_library.homepage'),
        ),
        migrations.RenameModel(
            old_name='OrderedPost',
            new_name='PostWithPosition',
        ),
        migrations.AlterField(
            model_name='postwithposition',
            name='home_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_library.homepage'),
        ),
    ]