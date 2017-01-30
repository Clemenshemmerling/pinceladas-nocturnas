from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^galeria/', views.galeria, name='galeria'),
	url(r'^galeria/(?P<pk>[0-9]+)/$', views.galeria_detail, name='galeria_detail'),
	url(r'^contact/', views.contacto, name='contact'),
	url(r'^planetario/', views.planetario, name='planetario'),
	url(r'^service/', views.service, name='service'),
	url(r'^about/', views.about, name='about'),
	url(r'^astronomy/', views.astronomy, name='astronomy'),
	url(r'^astrophotography/', views.astrophotography, name='astrophotography'),
	url(r'^prints/', views.prints, name='prints'),
	url(r'^deep_sky/', views.deep_sky, name='deep_sky'),
	url(r'^planetary/', views.planetary, name='planetary'),
	url(r'^wield_field/', views.wield_field, name='wield_field'),
	url(r'^landscape/', views.landscape, name='landscape'),
]
