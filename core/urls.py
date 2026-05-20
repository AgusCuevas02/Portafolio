from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('descargar-cv/', views.descargar_cv, name='descargar_cv'),
]