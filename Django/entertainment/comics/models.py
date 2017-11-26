# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.core.urlresolvers import reverse_lazy,reverse

# Create your models here.



class comics(models.Model):
	name=models.CharField(max_length=120)
	logo=models.FileField()
	 
	def __str__(self):
	   return self.name

	def get_absolute_url(self):
		return reverse_lazy('comics:index')
	       

class characters(models.Model):
	comics=models.ForeignKey(comics,on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	logo=models.FileField()
	abilities=models.CharField(max_length=500)
	
	def __str__(self):
		return self.name
