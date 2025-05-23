# Generated by Django 5.1.7 on 2025-04-21 07:35

import autoslug.fields
import django.db.models.deletion
import wagtail.fields
import wagtail.search.index
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title')),
                ('small_description', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_recommended', models.BooleanField(default=False)),
                ('image', models.ImageField(default=None, null=True, upload_to='portfolio/blog')),
                ('content', wagtail.fields.StreamField([('paragraph', 0), ('h4', 1), ('h6', 2), ('ordered_list', 3), ('unordered_list', 4), ('blockquote_1', 5), ('image', 6)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'features': ['p', 'a']}), 1: ('wagtail.blocks.CharBlock', (), {'features': ['h4']}), 2: ('wagtail.blocks.CharBlock', (), {'features': ['h6']}), 3: ('wagtail.blocks.RichTextBlock', (), {'features': ['ol']}), 4: ('wagtail.blocks.RichTextBlock', (), {'features': ['ul']}), 5: ('wagtail.blocks.CharBlock', (), {}), 6: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': '800 x 600', 'label': 'Image'})}, null=True)),
                ('total_visit', models.IntegerField(blank=True, null=True)),
                ('reading_time', models.IntegerField(blank=True, null=True)),
                ('meta_key', models.TextField(blank=True, max_length=100, null=True)),
                ('meta_desc', models.TextField(blank=True, max_length=160, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_category', to='news.newscategory')),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
