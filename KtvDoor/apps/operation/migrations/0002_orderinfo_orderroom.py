# Generated by Django 2.0 on 2019-11-04 13:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_privateroompackage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='订单编号')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='联系电话')),
                ('pay_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='支付时间')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='OrderRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_room', to='operation.OrderInfo', verbose_name='订单')),
                ('private_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.PrivateRoom', verbose_name='包房')),
                ('room_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.PrivateRoomPackage', verbose_name='包房套餐')),
            ],
            options={
                'verbose_name': '订单的房型',
                'verbose_name_plural': '订单的房型',
            },
        ),
    ]
