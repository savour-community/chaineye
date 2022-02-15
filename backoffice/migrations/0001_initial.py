# Generated by Django 2.2.3 on 2022-02-15 23:56

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('img', models.ImageField(blank=True, null=True, upload_to='message_img/%Y/%m/%d/', verbose_name='图片')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览次数')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否是有效')),
            ],
            options={
                'verbose_name': '公告表',
                'verbose_name_plural': '公告表',
            },
        ),
    ]