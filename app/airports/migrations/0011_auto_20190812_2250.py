# Generated by Django 2.2.4 on 2019-08-12 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0010_auto_20190811_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequency',
            name='icao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airports.Airport'),
        ),
        migrations.AlterField(
            model_name='runway',
            name='icao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airports.Airport'),
        ),
    ]
