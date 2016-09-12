from django.http import HttpResponse
from django.template import loader
from .models import Galeria
# Create your views here.

def galeria(request):
	galeria = Galeria.objects.order_by('id')
	template = loader.get_template('base.html')
	ctn = {
		'galeria': galeria
	}

	return HttpResponse(template.render(ctn, request))