# Generated by Django 2.2.6 on 2019-10-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS361WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='color',
            field=models.CharField(max_length=7),
        ),
    ]
