from django.contrib import admin
from django.urls import path
from . import views  # 确保导入正确的应用名称

urlpatterns = [
    path('', views.testmysql),  # 配置视图函数
]