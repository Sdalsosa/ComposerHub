# Generated by Django 3.2 on 2023-01-17 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compositions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='composition',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='composition',
            old_name='created',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='composition',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archive_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='composition',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tune_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='composition',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AddField(
            model_name='composition',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='composition',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
