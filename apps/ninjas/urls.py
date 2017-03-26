from django.conf.urls import url
from . import views

# Models --views --TEMPLATES
app_name = "ninjas"
urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^ninjas$', views.ninjas, name='my_ninjas'),
    url(r'^ninjas/(?P<color>[a-zA-Z]+)$', views.solo, name='my_solo'),
    url(r'^ninjas.*$', views.april, name='my_april')
]
