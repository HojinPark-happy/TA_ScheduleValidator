# Generated by Django 2.2.6 on 2019-12-05 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CS361WebApp', '0002_auto_20191205_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savepriority',
            name='myList',
        ),
    ]