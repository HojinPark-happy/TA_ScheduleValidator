# Generated by Django 2.2.6 on 2019-12-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS361WebApp', '0004_auto_20191205_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='savepriority',
            name='day',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='savepriority',
            name='end',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='savepriority',
            name='instructor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='savepriority',
            name='start',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]