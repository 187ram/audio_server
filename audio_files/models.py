from django.db import models
from django.core.exceptions import ValidationError

# validation for name, duration and participants

def name_validation(value):
    if value.split('.')[1] == 'mp3':
        return value
    else:
        raise ValidationError("Please provide proper file type")

def duration_validation(value):
    if value.days >= 0:
        return value
    else:
        raise ValidationError("Please provide duration in positive no")


def participant_validation(value):
    if len(value.split(',')) <= 10 or len(max(value.split(','))) <= 100:
        raise ValidationError("Max length of participant is 10 and their name is 100")
    else:
        return value

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=100,)
    duration = models.DurationField(validators =[duration_validation])
    upload_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.name


class Podcast(models.Model):
    name = models.CharField(max_length=100,)
    duration = models.DurationField(validators =[duration_validation])
    upload_date = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100,)
    participants = models.CharField(max_length=1000,)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.name


class Audiobook(models.Model):
    name = models.CharField(max_length=100,)
    author = models.CharField(max_length=100,)
    narrator = models.CharField(max_length=100,)
    duration = models.DurationField(validators =[duration_validation])
    upload_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.name

