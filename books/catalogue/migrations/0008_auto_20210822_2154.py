# Generated by Django 3.2.6 on 2021-08-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20210822_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='isbn10',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='isbn13',
            field=models.IntegerField(null=True),
        ),
    ]