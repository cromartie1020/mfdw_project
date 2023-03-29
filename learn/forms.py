from django import forms  
from .models import Entry, Topic

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields='__all__'
        
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['text'] 
        
               
         