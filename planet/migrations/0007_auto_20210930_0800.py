# Generated by Django 2.2.7 on 2021-09-30 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0006_courseartcle_comment_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseartcle',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='是否是有效'),
        ),
    ]
