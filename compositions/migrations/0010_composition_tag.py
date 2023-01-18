# Generated by Django 3.2 on 2023-01-18 12:46

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('compositions', '0009_auto_20230118_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
