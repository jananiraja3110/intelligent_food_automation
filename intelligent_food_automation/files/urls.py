from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('upload/', views.file_upload, name='file_upload'),
    path('', views.file_list, name='file_list'),
    path('<uuid:file_id>/', views.file_detail, name='file_detail'),
    path('<uuid:file_id>/download/', views.download_file, name='download_file'),
]