# Generated by Django 2.2.3 on 2022-05-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0009_auto_20220219_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='particle_num',
            field=models.PositiveIntegerField(default=0, verbose_name='预计课程数量'),
        ),
    ]