from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created']
    list_filter = ['completed', 'created']
    search_fields = ['title', 'description']
    date_hierarchy = 'created'
    ordering = ['completed', '-created']
    readonly_fields = ['created']
    list_editable = ['completed']
    list_per_page = 10
    list_max_show_all = 100

