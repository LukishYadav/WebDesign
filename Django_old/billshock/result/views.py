# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Output

# Create your views here.

def hello(request):
	output=Output.objects.all()
	Context={'output':output}
	#return HttpResponse("Hello from App")
	return render(request,'result/index.html',Context)


def hellom(request):
	#return HttpResponse('Hello')
	return render(request,'result/indexm.html')	