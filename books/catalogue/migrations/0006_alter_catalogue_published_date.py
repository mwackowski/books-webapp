# Generated by Django 3.2.6 on 2021-08-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_alter_catalogue_front_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='published_date',
            field=models.DateField(null=True),
        ),
    ]