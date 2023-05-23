from django.contrib import admin
from .models import LibraryUser, KnowledgeUser
# Register your models here.



@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ['UserName', 'PassWord', 'Name', 'Age', 'Gender', 'Phone', 'Email', 'Comment']
    search_fields = ['UserName']


@admin.register(KnowledgeUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ['UserName', 'PassWord', 'Name', 'Age', 'Gender', 'Phone', 'Email', 'Comment']
    search_fields = ['UserName']

@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """
    该类用于显示 admin 内置的 django_admin_log 表。
    其中，content_type 是指用户修改的 Model 名
    """
    list_display = ['action_time', 'user', 'content_type', '__str__']
    list_display_links = ['action_time']
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 15
    readonly_fields = ['action_time', 'user', 'content_type',
                       'object_id', 'object_repr', 'action_flag', 'change_message']

