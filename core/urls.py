from django.urls import include, path
from . import views
urlpatterns = [
path('evento/', views.evento, name='evento'),
]