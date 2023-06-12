from django.contrib import admin
from todo_app.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')

admin.site.register(Task, TaskAdmin)