# Generated by Django 2.2.3 on 2022-10-07 05:22

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_newsletter_is_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
    ]
