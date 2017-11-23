# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.core.urlresolvers import reverse


class Output(models.Model):
 BRM_BILLER_ACCOUNT_T_ACCOUNT_NO=models.CharField(max_length=250)
 BRM_BILLINFO_T_ACTG_CYCLE_DOM=models.CharField(max_length=250)
 TOTAL_AMOUNT=models.CharField(max_length=250)
 THRESHOLD=models.CharField(max_length=250)
 WEIGHTED_THRESHOLD=models.CharField(max_length=250)
 BILLSHOCK=models.CharField(max_length=250)
 PROXIMITY=models.CharField(max_length=250)
 def __str__(self):
 	return self.BRM_BILLER_ACCOUNT_T_ACCOUNT_NO+'-'+self.PROXIMITY

 def get_absolute_url(self):
    return reverse('result:detail',kwargs={'pk':self.pk}) 	
 	

# Create your models here.







