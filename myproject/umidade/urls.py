from django.urls import path
from . import views

urlpatterns = [
    path('receber/', views.receber_telemetria, name='receber_telemetria'),
]
