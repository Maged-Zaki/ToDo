from django.contrib import admin
from .models import Task, ConnectedUsers
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    model = "task"
    list_display = ["content", "date_created", "finish_time"]

admin.site.register(Task, TaskAdmin)
admin.site.register(ConnectedUsers)

