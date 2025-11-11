from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('vendor', 'Vendor'),
        ('purchase', 'Purchase Team'),
        ('tech', 'Tech Team'),
        ('production', 'Production Team'),
        ('admin', 'Admin Team'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"