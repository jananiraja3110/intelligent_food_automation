from django.contrib import admin
from .models import EncryptedFile, FileTransfer

@admin.register(EncryptedFile)
class EncryptedFileAdmin(admin.ModelAdmin):
    list_display = ['original_filename', 'user', 'file_type', 'file_size', 'uploaded_at']
    list_filter = ['file_type', 'uploaded_at']
    search_fields = ['original_filename', 'user__username']

@admin.register(FileTransfer)
class FileTransferAdmin(admin.ModelAdmin):
    list_display = ['file', 'from_user', 'to_team', 'status', 'created_at']
    list_filter = ['to_team', 'status', 'created_at']
    search_fields = ['file__original_filename', 'from_user__username']