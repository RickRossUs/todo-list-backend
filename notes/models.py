from django.db import models
from django.contrib.auth import get_user_model

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    checked = models.BooleanField(default=False, null=True, blank=True)
    date = models.DateTimeField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
