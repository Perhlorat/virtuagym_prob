# Generated by Django 2.0.7 on 2018-08-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Datetime updated'),
        ),
    ]
