from django.contrib import admin
from tasks.models import Category, Participant, Event
admin.site.register(Category)
admin.site.register(Participant)
admin.site.register(Event)

# Register your models here.
