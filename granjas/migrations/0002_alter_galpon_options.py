# Generated by Django 3.2 on 2021-04-17 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granjas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galpon',
            options={'managed': True, 'ordering': ['granja', 'numero'], 'verbose_name_plural': 'galpones'},
        ),
    ]