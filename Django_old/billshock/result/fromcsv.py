import csv,sys,os
project_dir="C:/Users/lukish.rajesh.yadav/Desktop/Django/1/billshock/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django
django.setup()


from result.models import Output


f = open('C:/Users/lukish.rajesh.yadav/Desktop/Django/1/billshock/input.csv','r')  
for line in f:  
   line =  line.split(',')  
   product = Output()  
   product.BRM_BILLER_ACCOUNT_T_ACCOUNT_NO = line[0]  
   product.PROXIMITY = line[6]   #data is missing from file  
   product.save()  

f.close()  


