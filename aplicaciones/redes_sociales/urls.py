from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('reguistrarEncuesta/', views.reguistrarEncuesta, name = 'reguistrarEncuesta'),
    path('estadisticas/', views.estadisticas, name = 'estadisticas'),
    path('estadisticas/vacio', views.estadisticas, name = 'vacio'),
]