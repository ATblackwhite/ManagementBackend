# Generated by Django 3.2 on 2023-05-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examine', '0002_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=30, verbose_name='用户名')),
                ('PassWord', models.CharField(max_length=30, verbose_name='密码')),
                ('Name', models.CharField(max_length=30, verbose_name='姓名')),
                ('Age', models.IntegerField(verbose_name='年龄')),
                ('Gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别')),
                ('Phone', models.CharField(max_length=30, verbose_name='电话')),
                ('Email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('Comment', models.BooleanField(verbose_name='是否可评论')),
            ],
            options={
                'verbose_name_plural': '博物馆系统用户',
            },
        ),
    ]
