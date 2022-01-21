# Generated by Django 2.2.7 on 2021-09-29 13:10

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='last_answer',
        ),
        migrations.AlterField(
            model_name='answers',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
