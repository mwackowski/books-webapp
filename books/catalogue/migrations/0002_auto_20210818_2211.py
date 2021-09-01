# Generated by Django 3.2.6 on 2021-08-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='isbn10',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogue',
            name='isbn13',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogue',
            name='published_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]