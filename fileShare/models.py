from django.db import models


# Create your models here.

class FileModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True,upload_to="img/")
    
    date = models.DateField(blank=True, null=True)
        
    def __str__(self):
        return self.title