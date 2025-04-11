from django.contrib import admin
from django.urls import path
from . import views  # 确保导入正确的应用名称

urlpatterns = [
    path('', views.gradio_page),
    path('getModelbyPicInput/', views.getModelbyPicInput, name='getModelbyPicInput'),
    path('infer/', views.upload_and_infer, name='upload_and_infer'),
]