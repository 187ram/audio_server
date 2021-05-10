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
    if len(value.split(',')) > 10:
        raise ValidationError("max no of participants is 10")
    elif len(max(value.split(','))) > 100:
        raise ValidationError("Name should be less than 100")
    else:
        return value

# Create your models here.
class Audiobook(models.Model):
    name = models.CharField(max_length=100,)
    author = models.CharField(max_length=100,)
    narrator = models.CharField(max_length=100,)
    duration = models.DurationField(validators =[duration_validation])
    uploaded_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.name


class Podcast(models.Model):
    name = models.CharField(max_length=100,)
    duration = models.DurationField(validators =[duration_validation])
    uploaded_time = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100,)
    participants = models.CharField(max_length=1100, blank=True,validators=[participant_validation])
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100,)
    duration = models.DurationField(validators =[duration_validation])
    uploaded_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.name



