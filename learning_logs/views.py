from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """a view function that takes in information from request and then prepare the data and sends it to the 
    browser by using the template which tells django how you want the page to be structured"""
    return render(request, 'learning_logs/index.html') #render is a module that renders information based on the data 
    # provided in the view file

def topics(request):
    """shows all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """it handles the request of individual pages using 
    their topic_id which is an interger as the second argument"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ a view function that handles the request of
    adding a new topic by the user
    """
    if request.method != 'POST':
        #That is, no data is submitted; create a blank form.
        form = TopicForm()
    else:
        #POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form': form}
    return render(request, 'learning-logs/new_topic.html', context)

def new_entry(request, topic_id):
    """it handles the logic for adding a new entry to a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #no data has been submitted; create a blank entry form
        form = EntryForm()
    else:
        #POST data was submitted, so request will be processed
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #initial request; prefill form with the current entry
        form = EntryForm(instance=entry)
    else:
        #Post data was submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
