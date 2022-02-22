# Generated by Django 2.2.3 on 2022-02-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0008_course_is_pre_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_synced',
            field=models.BooleanField(default=False, verbose_name='是否已经同步'),
        ),
        migrations.AddField(
            model_name='courseartcle',
            name='is_synced',
            field=models.BooleanField(default=False, verbose_name='是否已经同步'),
        ),
    ]