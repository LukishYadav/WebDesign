from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Album

class IndexView(generic.ListView):
	template_name='music/index.html'
	context_object_name='album_all'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model=Album
	#context_object_name='album2'
	template_name='music/detail.html'

class AlbumCreate(CreateView):
	model=Album
	fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	model=Album
	fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
	model=Album
	success_url=reverse_lazy('music:index')
