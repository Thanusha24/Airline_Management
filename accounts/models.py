from django.conf import settings 
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Snippet(models.Model):
	Name=models.CharField(max_length=50,default="john")
	Email=models.EmailField(default="john@gmail.com")
	Source=models.CharField(max_length=50,default="BANGALORE")
	Destination=models.CharField(max_length=50,default="DELHI")
	Departure=models.DateTimeField(default=timezone.now())
	Arrival=models.DateTimeField(blank=True, null=True)
	def publish(self):
        	self.Arrival = timezone.now()
        	self.save()

