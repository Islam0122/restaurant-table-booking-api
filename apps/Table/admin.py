from django.contrib import admin
from .models import Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats', 'location')
    list_filter = ('location',)
    search_fields = ('name', 'location')
    ordering = ('name',)
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('name', 'seats', 'location')
        }),
    )
