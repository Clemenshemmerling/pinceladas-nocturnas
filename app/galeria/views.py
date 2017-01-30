from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Galeria
# Create your views here.

def index(request):
	galeria = Galeria.objects.order_by('id')
	template = loader.get_template('index.html')
	title = 'Pinceladas Nocturnas'
	ctn = {
		'galeria': galeria,
		'title': title
	}

	return HttpResponse(template.render(ctn, request))

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

def contacto(request):
	template = loader.get_template('contact.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def planetario(request):
	template = loader.get_template('planetario.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def service(request):
	template = loader.get_template('services.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def about(request):
	template = loader.get_template('about.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def about(request):
	template = loader.get_template('about.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def astronomy(request):
	template = loader.get_template('astronomy.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def astrophotography(request):
	template = loader.get_template('astrophotography.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def prints(request):
	template = loader.get_template('prints.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def deep_sky(request):
	template = loader.get_template('deep_sky.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def planetary(request):
	template = loader.get_template('planetary.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def wield_field(request):
	template = loader.get_template('wield_field.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))

def landscape(request):
	template = loader.get_template('landscape.html')
	title = 'Contact'
	ctn = {
		'title:': title
	}

	return HttpResponse(template.render(ctn, request))
