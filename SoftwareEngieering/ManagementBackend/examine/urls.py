from django.urls import path, re_path
from . import views
from django.views.static import serve
urlpatterns = [
    path('list/', views.examine_list),
    path('accept/', views.accept_op),
    path('reject/', views.reject_op),
]