# Generated by Django 3.2.6 on 2021-08-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20210822_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
