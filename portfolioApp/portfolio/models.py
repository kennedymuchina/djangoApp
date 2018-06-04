
from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length = 50)
    short_description = models.CharField(max_length = 100, null = True, blank = True)
    details = models.TextField()
    start_date = models.DateTimeField(blank = True, null = True)
    finished_date = models.DateTimeField(auto_now_add = True)
    thumbnail = models.ImageField(null = True, blank = True, upload_to = 'media')
    project_files = models.ImageField(null = True, blank = True, upload_to = 'media')
    cliente = models.CharField(default = 'Personal Project', null = True, blank = True, max_length = 100)

    def __str__(self):
        return self.title
