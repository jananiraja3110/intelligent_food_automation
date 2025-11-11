import uuid
from django.db import models
from django.conf import settings

class EncryptedFile(models.Model):
    FILE_TYPE_CHOICES = [
        ('raw_material', 'Raw Material Data'),
        ('dataset', 'Dataset'),
        ('excel', 'Excel File'),
        ('csv', 'CSV File'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    original_filename = models.CharField(max_length=255)
    encrypted_file = models.BinaryField()  # Store encrypted data
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    file_size = models.IntegerField()  # Size in bytes
    uploaded_at = models.DateTimeField(auto_now_add=True)
    encryption_key = models.BinaryField()  # Store encrypted key
    
    def __str__(self):
        return f"{self.original_filename} ({self.user.username})"

class FileTransfer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]
    
    # Define role choices here (same as in users model)
    ROLE_CHOICES = [
        ('vendor', 'Vendor'),
        ('purchase', 'Purchase Team'),
        ('tech', 'Tech Team'),
        ('production', 'Production Team'),
        ('admin', 'Admin Team'),
    ]
    
    file = models.ForeignKey(EncryptedFile, on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_transfers', on_delete=models.CASCADE)
    to_team = models.CharField(max_length=20, choices=ROLE_CHOICES)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Transfer {self.file.original_filename} to {self.to_team}"