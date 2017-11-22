# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Output
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

def hello(request):
	output=Output.objects.all()
	Context={'output':output}
	#return HttpResponse("Hello from App")
	return render(request,'result/index.html',Context)


def hellom(request):
	#return HttpResponse('Hello')
	return render(request,'result/indexm.html')


class listview(generic.ListView):
	template_name='result/indexm.html'

	def get_queryset(self):
		return Output.objects.all()

class detailview(generic.DetailView):
	model=Output
	template_name='result/index.html'

