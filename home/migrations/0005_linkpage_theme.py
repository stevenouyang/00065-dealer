# Generated by Django 5.1.7 on 2025-05-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_linkitem_text_content_linkpage_background_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpage',
            name='theme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', max_length=10),
        ),
    ]
