from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.galeria, name='galeria'),
	url(r'^galeria/(?P<pk>[0-9]+)/$', views.galeria_detail, name='galeria_detail'),
]