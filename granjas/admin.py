from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Avicola, Galpon, Granja


class GranjaInline(admin.TabularInline):
    model = Granja
    extra = 1


class AvicolaAdmin(SimpleHistoryAdmin):
    history_list_display = ['nombre', ]
    inlines = [GranjaInline, ]

    class Meta:
        model = Avicola


class GalponInline(admin.TabularInline):
    model = Galpon
    extra = 1


class GranjaAdmin(SimpleHistoryAdmin):
    inlines = [GalponInline, ]
    list_filter = ['avicola', ]

    class Meta:
        model = Granja


class GalponAdmin(SimpleHistoryAdmin):
    list_filter = ['granja', ]

    class Meta:
        model = Galpon


admin.site.register(Avicola, AvicolaAdmin)
admin.site.register(Granja, GranjaAdmin)
admin.site.register(Galpon, GalponAdmin)
