# Generated by Django 2.2.6 on 2019-12-05 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS361WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavePriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myList', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='coursetime',
            name='instructor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='TA',
        ),
    ]
