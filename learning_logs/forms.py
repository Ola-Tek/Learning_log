from django import forms #imported the forms module
from .models import Topic, Entry #import the models we are working on

class TopicForm(forms.Modelform):
    """this is a class that helps us to build forms
    which will be used by the users to add new topics that they've 
    learnt
    """
    class meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """creating a form wheere a new entry can be entered"""
    class meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} #widget is an html element attriibute such as a single line text, multi-line text area
        #or single drop list. By adding the widget attribute, we are overiding the default setting of django customizing it to a maximum 80
        #colums wide.