# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.core.urlresolvers import reverse_lazy,reverse

from models import comics

def main(request):
	return render(request,'comics/main.html')


class index(generic.ListView):
	template_name="comics/index.html"

	def get_queryset(self):
		return comics.objects.all()	


class detail(generic.DetailView):
	model=comics
	template_name="comics/detail.html"


class addcomics(CreateView):
	model=comics
	fields=['name','logo']

class deletecomics(DeleteView):
	model=comics
	fields=['name','logo']
	success_url=reverse_lazy('comics:index')	
# Create your views here.
