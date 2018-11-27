from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^species', views.getSpecies),
    url(r'^age', views.getAges),
    url(r'^audio', views.getAudio),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
