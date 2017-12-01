from django.http import HttpResponse
from django.shortcuts import render


def hello2(request):
	#return HttpResponse('Hello')
	return render(request,'index.html')