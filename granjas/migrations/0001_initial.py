# Generated by Django 3.2 on 2021-04-17 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avicola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'avícolas',
                'db_table': 'avicolas',
                'ordering': ['nombre'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Granja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('superficie', models.DecimalField(decimal_places=2, max_digits=9)),
                ('avicola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='granjas', to='granjas.avicola')),
            ],
            options={
                'db_table': 'granjas',
                'ordering': ['nombre'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Galpon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(verbose_name='número')),
                ('granja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galpones', to='granjas.granja')),
            ],
            options={
                'db_table': 'galpones',
                'ordering': ['granja', 'numero'],
                'managed': True,
            },
        ),
    ]
