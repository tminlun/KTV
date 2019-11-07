# Generated by Django 2.0 on 2019-11-04 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateRoomPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('private_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.PrivateRoom', verbose_name='房型')),
            ],
            options={
                'verbose_name': '包房套餐',
                'verbose_name_plural': '包房套餐',
            },
        ),
    ]