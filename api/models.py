from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    complition = models.BooleanField()
    tag = models.ManyToManyField('Tag')
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


