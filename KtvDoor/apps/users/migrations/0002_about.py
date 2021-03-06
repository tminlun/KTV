# Generated by Django 2.0 on 2019-11-04 11:12

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('describe', models.CharField(blank=True, max_length=100, null=True, verbose_name='描述')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='课程内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('about_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.AboutType', verbose_name='类型')),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
    ]
