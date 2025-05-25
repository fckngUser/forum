from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Articles(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()  
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        default=1  
    )
    created_at = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return self.name