# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 13:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0003_remove_profile_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comment_post',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='commented_image',
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='gram.Image'),
        ),
    ]