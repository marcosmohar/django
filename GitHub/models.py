from django.db import models

# Create your models here.
class Repositories(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=50)
    url = models.URLField()
    language = models.CharField(max_length=50)
    stars = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name