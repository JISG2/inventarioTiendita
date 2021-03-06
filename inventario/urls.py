from django.conf.urls import url
from rest_framework import routers
from inventario.views import *


urlpatterns = [
    url(r'^proteinas/$', proteinasView.as_view()),
    url(r'^proteinas/(?P<pk>\d+)/?$', proteinasView2.as_view()),
    url(r'^aminoacidos/$', aminoacidosView.as_view()),
    url(r'^aminoacidos/(?P<pk>\d+)/?$', aminoacidosView2.as_view()),
    url(r'^glutaminas/$', glutaminasView.as_view()),
    url(r'^glutaminas/(?P<pk>\d+)/?$', glutaminasView2.as_view())
]