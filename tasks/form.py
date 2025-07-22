from django import forms
from tasks.models import Event, Participant,Category

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','description','due_date','location','category']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'formDesign',
                'placeholder' : 'Ener your name',
                
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'formDesign',
                'placeholder' : "Descriptions"
            }),
            'due_date' : forms.SelectDateWidget(),
            'location' : forms.TextInput(attrs={
                'class' : 'formDesign'
            })
        }
        labels = {
            'name' : "Event Name",
            'description' : "Event Description"
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']
        labels = {
            'name' : "Category Name",
            'description' : "Category Description"
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name','email','event']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'part-form',
                'placeholder' : 'Your Name'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'part-form',
                'placeholder' : 'example@gmail.com'
            })
            
        }
        labels = {
            'name' : 'Participant\'s Name',
            'email' : 'Participant\'s Email'
        }