# Generated by Django 2.2.10 on 2020-04-07 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('js_showcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcasesection',
            name='background_video_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Background Video URL'),
        ),
    ]
