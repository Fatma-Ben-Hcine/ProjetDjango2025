from django.urls import path 
from . import views 

app_name = 'qcm'
urlpatterns = [ 
path('<int:qcm_id>/', views.afficher_qcm, name='questions'),
path('<int:qcm_id>/soumettre/', views.soumettre_qcm, name='soumettre_qcm'),

]