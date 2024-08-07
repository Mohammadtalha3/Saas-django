from django.db import models

# Create your models here.

class Page_Vists(models.Model):
    path = models.TextField(blank = True, null= True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label= 'visits'  #it is to tell tahat it does belongs to this app 

    

