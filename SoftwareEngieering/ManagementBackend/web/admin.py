from django.contrib import admin
from .models import *
# Register your models here.
class DataManager(admin.ModelAdmin):
    # 列表页显示哪些字段列
    list_display = ['id', 'object_name', 'makers_name', 'museum', 'time_period', 'label', 'credit']

    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['object_name']

    # 添加过滤器
    list_filter = ['museum']

    # 添加搜索框 进行[模糊查询]
    search_fields = ['object_name']

    # 添加可在列表页编辑的字段 要与链接的字段相斥
    # list_editable = ['account']

    # 每页显示数据
    list_per_page = 10

#
# class UserManager(admin.ModelAdmin):
#     # 列表页显示哪些字段列
#     list_display = ['user_id', 'user_password', 'user_name', 'user_sex', 'user_tel', 'user_comment', 'user_login']
#
#     # 控制list_display中的字段 哪些可以链接到修改页
#     list_display_links = ['user_name']
#
#     # 添加过滤器
#     list_filter = ['user_sex']
#
#     # 添加搜索框 进行[模糊查询]
#     search_fields = ['user_name']
#
#     # 添加可在列表页编辑的字段 要与链接的字段相斥
#     # list_editable = ['account']
#
#     # 每页显示数据
#     list_per_page = 10


admin.site.register(CulturalRelicsData, DataManager)

# admin.site.register(User, UserManager)