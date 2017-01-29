from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^galeria_fotos/', views.galeria, name='galeria'),
	url(r'^galeria/(?P<pk>[0-9]+)/$', views.galeria_detail, name='galeria_detail'),
]
