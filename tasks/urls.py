from django.urls import path
from tasks.views import show, home,dashboard,details,addEvent,participant

urlpatterns = [
    path('show', show),
    path('', home, name= 'home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('details/<int:id>/', details, name='details'),
    path('addevent/',addEvent, name= 'addevent' ),
    path('participant/<int:id>', participant, name= 'participant')
   
]
