# Generated by Django 3.2 on 2021-04-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granjas', '0004_auto_20210419_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='granja',
            name='capacidad',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='historicalgranja',
            name='capacidad',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]