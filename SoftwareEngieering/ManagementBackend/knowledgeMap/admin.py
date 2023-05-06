from django.contrib import admin
from .models import *
# Register your models here.
class CollectionsManager(admin.ModelAdmin):
    # 列表页显示哪些字段列
    list_display = ['id', 'collection_name', 'museum', 'materials', 'creation_date', 'discription', 'image_url']

    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['collection_name']

    # 添加过滤器
    list_filter = ['museum']

    # 添加搜索框 进行[模糊查询]
    search_fields = ['name']

    # 添加可在列表页编辑的字段 要与链接的字段相斥
    # list_editable = ['account']

    # 每页显示数据
    list_per_page = 10


admin.site.register(Collections, CollectionsManager)