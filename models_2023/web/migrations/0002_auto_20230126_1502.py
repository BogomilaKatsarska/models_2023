# Generated by Django 3.2.16 on 2023-01-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
