from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Galeria
# Create your views here.

def galeria(request):
	galeria = Galeria.objects.order_by('id')
	template = loader.get_template('galeria.html')
	title = 'Galeria de fotos Pinceladas Nocturnas'
	ctn = {
		'galeria': galeria,
        'title': title
	}

	return HttpResponse(template.render(ctn, request))

def galeria_detail(request, pk):
	galeria = get_object_or_404(Galeria, pk=pk)
	template = loader.get_template('galeria_detail.html')
	title = 'Galeria de fotos Pinceladas Nocturnas'
	ctn = {
		'galeria': galeria,
		'title': title
	}

	return HttpResponse(template.render(ctn, request))