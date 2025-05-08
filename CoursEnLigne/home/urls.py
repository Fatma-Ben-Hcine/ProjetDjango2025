from django.urls import path,include 
from . import views 
urlpatterns = [ 
path('', views.index, name='index'),
path('lesson/', include('lesson.urls', namespace='lesson')),
path('qcm/',include('qcm.urls',namespace='qcm')), 
] 