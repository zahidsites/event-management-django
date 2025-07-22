from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    event = models.ManyToManyField(Event, related_name= "events")

class Category(models.Model):
    choice_options = (
        ('music','music'),
        ('drama','drama'),
        ('party','party')
    )
    name = models.CharField(max_length=255, choices=choice_options, default='drama')
    description = models.TextField()

    def __str__(self):
        return self.name
   