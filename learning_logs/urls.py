from django.conf.urls import url
from . import views

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),
    #for the topics page to show all topic
    url(r'^topics/$', views.topics, name='topics'),

    #individaula topic pages
    url(r'^topics/(?p<topic_id>\d+)/$', views.topics, name='topic'),
    #page for adding a new topic by users
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #page for adding a new entry by new users
    url(r'^new_entry/(?p<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #page for editing new entry
    url(r'^edit_entry/(?p<entry_id>|d+)/$', views.edit_entry, name='edit_entry'),
]