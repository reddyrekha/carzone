from django.db import models

# Create your models here.
class team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'photos/%Y/%M/%D/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_link=models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name