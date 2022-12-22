from django.db import models

# Create your models here.
class BlogData(models.Model):
    heading = models.CharField(default='completely random notes',max_length=500)
    category = models.CharField(default='life should have meaning',max_length=50)
    image = models.ImageField(upload_to='photos')
    place = models.CharField(default='Earth',max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(default='',max_length=10000)
    highlights = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.heading

