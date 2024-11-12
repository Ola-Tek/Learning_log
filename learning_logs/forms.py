from django import forms  # imported the forms module
from .models import Topic, Entry  # import the models we are working on

class TopicForm(forms.ModelForm):
    """This class helps us build forms
    which will be used by users to add new topics that they've 
    learned.
    """
    class Meta:  # Corrected 'meta' to 'Meta'
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # Optionally, you can customize the label

class EntryForm(forms.ModelForm):
    """Creating a form where a new entry can be added."""
    class Meta:  # Corrected 'meta' to 'Meta'
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # Optionally, you can customize the label
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80})  # Customize the widget
        }  # Widget is an HTML element attribute such as a single-line text or multi-line text area.
          # By adding the widget attribute, we are overriding the default setting of Django, customizing it to a maximum of 80
          # columns wide.
