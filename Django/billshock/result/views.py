# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Output
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
"""
def hello(request):
	output=Output.objects.all()
	Context={'output':output}
	#return HttpResponse("Hello from App")
	return render(request,'result/index.html',Context)
"""

def hellom(request):
	#return HttpResponse('Hello')
	return render(request,'result/main.html')


class listview(generic.ListView):
	template_name='result/indexm.html'

	def get_queryset(self):
		return Output.objects.all()



class detailview(generic.DetailView):
	model=Output
	template_name='result/index.html'


class add(CreateView):
	model=Output
	fields=['BRM_BILLER_ACCOUNT_T_ACCOUNT_NO','PROXIMITY']


class delete(DeleteView):
	model=Output
	fields=['BRM_BILLER_ACCOUNT_T_ACCOUNT_NO','PROXIMITY']
	success_url = reverse_lazy('result:hello')
	