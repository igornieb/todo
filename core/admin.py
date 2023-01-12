from django.contrib import admin
from core.models import Task, Account


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('owner', 'task')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
