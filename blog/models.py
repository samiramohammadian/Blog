from django.db import models
from django.conf import settings
import time

class Post(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = time.time()
        
    def __str__(self):
        return self.title