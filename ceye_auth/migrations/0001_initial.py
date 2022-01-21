# Generated by Django 2.2.7 on 2021-09-27 13:51

import common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('user_name', models.CharField(default='', max_length=32, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=128, verbose_name='密码')),
                ('token', models.CharField(default='', max_length=256, verbose_name='token')),
                ('token_is_expire', models.IntegerField(choices=[(1, 'EXPIRED'), (2, 'UNEXPIRE')], default=2)),
                ('phone', models.CharField(default='', max_length=16, verbose_name='手机')),
                ('loginip', models.CharField(default='', max_length=128, verbose_name='登陆IP')),
                ('regtime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='注册时间')),
                ('logintime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='登陆时间')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('real_name', models.CharField(default='', max_length=64, verbose_name='真实名字')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_img/%Y/%m/%d/', verbose_name='头像')),
                ('introduce', models.TextField(blank=True, default='', max_length=512, verbose_name='简介')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女'), ('未知', '未知')], default='未知', max_length=16, verbose_name='性别')),
                ('position', models.CharField(default='', max_length=16, verbose_name='职位')),
                ('company', models.CharField(default='', max_length=16, verbose_name='单位')),
                ('email', models.CharField(default='', max_length=128, verbose_name='邮件')),
                ('user_id', common.models.IdField(db_index=True, default='', max_length=100, verbose_name='用户ID')),
                ('qq', models.CharField(default='', max_length=128, verbose_name='QQ')),
                ('wechat', models.CharField(default='', max_length=128, verbose_name='微信')),
            ],
        ),
        migrations.CreateModel(
            name='UserWalletRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('amount', common.models.DecField(decimal_places=30, default=0, max_digits=65, verbose_name='提取金额')),
                ('coin_type', models.CharField(choices=[('Cny', 'Cny'), ('AngleCoin', 'AngleCoin')], default='Cny', max_length=32, verbose_name='币种类型')),
                ('source_type', models.CharField(choices=[('WeiChat', 'WeiChat'), ('ZhiFuBao', 'ZhiFuBao'), ('Reward', 'Reward')], default='WeiChat', max_length=16, verbose_name='渠道')),
                ('wallet_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw'), ('Reward', 'Reward')], default='Deposit', max_length=16, verbose_name='充提奖励类型')),
                ('check_status', models.CharField(choices=[('UnCheck', 'UnCheck'), ('Checking', 'Checking'), ('Checked', 'Checked'), ('Refuse', 'Refuse')], default='Checking', max_length=16, verbose_name='审核状态')),
                ('is_pay', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=16, verbose_name='是否已支付')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_withdraw', to='ceye_auth.User', verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '用户资金记录表',
                'verbose_name_plural': '用户资金记录表',
            },
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('coin_type', models.CharField(choices=[('Cny', 'Cny'), ('FishCoin', 'FishCoin')], default='Cny', max_length=32, verbose_name='钱包类型')),
                ('amount', common.models.DecField(decimal_places=30, default=0, max_digits=65, verbose_name='金额')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_gains', to='ceye_auth.User', verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '用户钱包表',
                'verbose_name_plural': '用户钱包表',
            },
        ),
    ]
