# Generated by Django 2.2.10 on 2020-04-15 10:31

from django.db import migrations
import js_showcase.models


class Migration(migrations.Migration):

    dependencies = [
        ('js_showcase', '0002_showcasesection_background_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcasecontainer',
            name='attributes',
            field=js_showcase.models.AttributesField(blank=True, default=dict, verbose_name='Attributes'),
        ),
        migrations.AddField(
            model_name='showcasesection',
            name='attributes',
            field=js_showcase.models.AttributesField(blank=True, default=dict, verbose_name='Attributes'),
        ),
        migrations.AddField(
            model_name='showcaseslide',
            name='attributes',
            field=js_showcase.models.AttributesField(blank=True, default=dict, verbose_name='Attributes'),
        ),
        migrations.AddField(
            model_name='showcaseslideshow',
            name='attributes',
            field=js_showcase.models.AttributesField(blank=True, default=dict, verbose_name='Attributes'),
        ),
    ]