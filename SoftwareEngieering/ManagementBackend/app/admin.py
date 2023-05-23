from django.contrib import admin
from .models import *
# Register your models here.
# class CommentsManager(admin.ModelAdmin):
#     # 列表页显示哪些字段列
#     list_display = ['username', 'wid', 'content', 'time']
#
#     # 控制list_display中的字段 哪些可以链接到修改页
#     list_display_links = ['username']
#
#     # 添加过滤器
#     # list_filter = ['museum']
#
#     # 添加搜索框 进行[模糊查询]
#     search_fields = ['username']
#
#     # 添加可在列表页编辑的字段 要与链接的字段相斥
#     # list_editable = ['account']
#
#     # 每页显示数据
#     list_per_page = 10


# class UsersManager(admin.ModelAdmin):
#     # 列表页显示哪些字段列
#     list_display = ['username', 'pwd', 'sex', 'age', 'address']
#
#     # 控制list_display中的字段 哪些可以链接到修改页
#     list_display_links = ['username']
#
#     # 添加过滤器
#     list_filter = ['sex']
#
#     # 添加搜索框 进行[模糊查询]
#     search_fields = ['username']
#
#     # 添加可在列表页编辑的字段 要与链接的字段相斥
#     # list_editable = ['account']
#
#     # 每页显示数据
#     list_per_page = 10

class WenwuManager(admin.ModelAdmin):
    # 列表页显示哪些字段列
    list_display = ['wname', 'visnum', 'id', 'date', 'description', 'website']

    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['wname']

    # 添加过滤器
    list_filter = ['visnum']

    # 添加搜索框 进行[模糊查询]
    search_fields = ['wname']

    # 添加可在列表页编辑的字段 要与链接的字段相斥
    # list_editable = ['account']

    # 每页显示数据
    list_per_page = 10

class WenwulikesManager(admin.ModelAdmin):
    # 列表页显示哪些字段列
    list_display = ['wid', 'username', 'shape']

    # 控制list_display中的字段 哪些可以链接到修改页
    list_display_links = ['username']

    # 添加过滤器
    # list_filter = ['user_sex']

    # 添加搜索框 进行[模糊查询]
    search_fields = ['username']

    # 添加可在列表页编辑的字段 要与链接的字段相斥
    # list_editable = ['account']

    # 每页显示数据
    list_per_page = 10

# admin.site.register(Comments, CommentsManager)
# admin.site.register(Users, UsersManager)
admin.site.register(Wenwu, WenwuManager)
admin.site.register(Wenwulikes, WenwulikesManager)