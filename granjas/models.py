from django.db import models
from simple_history.models import HistoricalRecords


class Avicola(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'avicolas'
        ordering = ['nombre']
        verbose_name_plural = 'avícolas'

    def __str__(self):
        return self.nombre


class Granja(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    avicola = models.ForeignKey(Avicola, related_name='granjas',
                                on_delete=models.CASCADE, null=False)
    superficie = models.DecimalField(
        max_digits=9, decimal_places=2, null=False)
    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'granjas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Galpon(models.Model):
    numero = models.PositiveIntegerField(verbose_name='número', null=False)
    granja = models.ForeignKey(
        Granja, related_name='galpones', on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'galpones'
        ordering = ['granja', 'numero']
        verbose_name_plural = 'galpones'

    def __str__(self):
        return f'Galpón {str(self.numero)} ({str(self.granja)})'
