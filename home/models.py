from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    location = models.CharField(max_length=200)
    frontImage = models.ImageField(upload_to='project_pics')
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.title} Project'


class Report(models.Model):
    name = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    file = models.FileField()



class Slideshow(models.Model):
    title = models.CharField(max_length=200)
    nutshell = models.TextField(null=True, blank=True)
    #date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='slideshow')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    name = models.CharField(max_length=200)
    #email = models.EmailField()
    #subject = models.CharField(max_length=200)
    comment = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return f'{self.name}'


class Gallery(models.Model):
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos')


