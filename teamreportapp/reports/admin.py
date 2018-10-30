from django.contrib import admin
from reports.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'date_created', 'date_completed')
    list_filter = ('status', 'date_completed')
    readonly_fields = ('date_created', 'date_completed')

admin.site.register(Project, ProjectAdmin)
