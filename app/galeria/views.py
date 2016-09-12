from django.http import HttpResponse
from django.template import loader
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
