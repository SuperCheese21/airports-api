# Generated by Django 2.2.4 on 2019-08-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0004_auto_20190811_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequency',
            name='frequency',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
