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
