from django.urls import path, re_path  # Update import

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Page to show all topics
    path('topics/', views.topics, name='topics'),

    # Individual topic pages
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # Corrected view name
    
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Page for adding a new entry by users
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # Updated to use path converters
    
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Updated to use path converters
]
