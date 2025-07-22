from django.shortcuts import render,redirect
from tasks.form import EventForm, CategoryForm, ParticipantForm
from tasks.models import Event,Participant
from django.contrib import messages
from django.db.models import Count,Q
from datetime import date

def show(request):
    
    return render(request,'test.html')


def home(request):
    events = Event.objects.annotate(pcount = Count('events'))
    context = {
        'events' : events
    }

    return render(request, 'home.html',context)



def details(request,id):
    detail = Event.objects.get(id = id)
    return render(request, 'details.html',{'detail' : detail})

# --------------------DASHBOARD-------------------

def dashboard(request):
    type = request.GET.get('type','all')

    base_query = Event.objects.select_related('category').prefetch_related('events')
    
    total_events = Event.objects.aggregate(total=Count('id'))
    total_participant = Participant.objects.aggregate(total=Count('id'))
    past_event = Event.objects.filter(due_date__lt=date.today()).aggregate(past_event_count=Count('id'))
    upcoming_event = Event.objects.filter(due_date__gt=date.today()).aggregate(upcoming = Count('id'))

    
    
    if type == 'all':
        allEvents = base_query.all()
    elif type == 'comingEvent':
        allEvents = base_query.filter(due_date__gt = date.today())
    elif type == 'pastEvent':
        allEvents = base_query.filter(due_date__lt = date.today())

    context = {
        'total' : total_events,
        't_part' : total_participant,
        'p_event' : past_event,
        'upcoming' : upcoming_event,
        'allEvents' : allEvents
    }
    return render(request, 'dashboard.html',context)

# -----------------------ADD EVENT------------------------------

def addEvent(request):
    event_form = EventForm()
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid(): 
            event_form.save()

    context = {
        'eventForm' : event_form,
    }
    return render(request, 'form.html', context)

# ----------------UPDATE EVENTS -------------

def updateEvent(request,id):
    eventId = Event.objects.get(id=id)
    event_form = EventForm(instance=eventId)
    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=eventId)
        if event_form.is_valid(): 
            event_form.save()
            messages.success(request,"Successful")
            return redirect('updateEvent', id)
            
    context = {
        'eventForm' : event_form,
    }
    return render(request, 'form.html', context)

# -------------------PARTICIPANT EVENT ----------------------

def participant(request,id):
    
    participant = ParticipantForm()
    if request.method == 'POST':
        participant = ParticipantForm(request.POST)
        if participant.is_valid():
            participant.save()
            messages.success(request,"Successful")
            return redirect('home')
    
    context = {
        'participant' : participant
    }
    return render(request, 'participant.html',context)

# ------------- Delete operations -------------------

def deleteEvent(request,id):
    if request.method == 'POST':
        del_ev = Event.objects.get(id=id)
        del_ev.delete()
        messages.success(request,'Delete Successful')
        return redirect('dashboard')