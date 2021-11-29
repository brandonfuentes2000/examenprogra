from django.conf.urls import url
from . import views

urlpatterns = [
   
    url('curso/nueva/', views.curso_nueva, name='curso_nueva'),
    ]