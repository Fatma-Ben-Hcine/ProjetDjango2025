from django.urls import path 
from . import views 
app_name = 'cours'
urlpatterns = [ 
path('', views.listeCours, name='liste'),
path('<int:cours_id>/', views.details_cours, name='detail'),

] 