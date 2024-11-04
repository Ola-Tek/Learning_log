from django.db import models

# Create your models here.
#a model is like a module
class Topic(models.Model):
    """we are creating a model called topic that tells us what the user is learning
    and each model class inherits a method called model from Model
    attr: a model class will be given set of rules to follow, example is the number of characters
    then also othe date
    """
    text = models.CharField(max_length=205) #this tells tells the number or amount of text or characters accepted
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a sting representation of the model"""
        return self.text
    
class Entry(models.Model):
    """a class that defines the entry and tells what the topic is associated with"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)# When the referenced object is deleted, 
    #also delete the objects that have this foreign key.
    #foreign key is an instance, its a data base term, it refers to another record in the database
    #each topic is assigned a key or id when created, django estaablishes a connection between the two pieces of data
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """meta holds exra information on managing a model"""
        verbose_name_plural = 'entries' #this is telling django to use the word entries when more than one entry is added
        #without this django would refer to multiple entries as 'entrys'

    def __str__(self):
        return self.text[:50] + "....." #the string representation of the model and tells the entry class to return the first fifty words