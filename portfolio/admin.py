from django.contrib import admin

from portfolio import models


# Register your models here.
@admin.register(models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'technology', 'conclusion_date')
    list_filter = ('technology', 'conclusion_date')
    search_fields = ('id', 'title', 'technology', 'conclusion_date')
    date_hierarchy = 'conclusion_date'
    ordering = ('conclusion_date',)
    readonly_fields = ('conclusion_date',)
    list_per_page = 10
