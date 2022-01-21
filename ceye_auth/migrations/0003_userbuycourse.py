# Generated by Django 2.2.7 on 2021-10-04 06:20

import common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ceye_auth', '0002_auto_20210930_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBuyCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('course_id', common.models.IdField(db_index=True, default='', max_length=100, verbose_name='购买的课程ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ceye_auth.User', verbose_name='购买人')),
            ],
            options={
                'verbose_name': '用户购买课程表',
                'verbose_name_plural': '用户购买课程表',
            },
        ),
    ]
