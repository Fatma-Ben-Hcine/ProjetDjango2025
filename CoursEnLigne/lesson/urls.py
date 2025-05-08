from django.urls import path 
from . import views 
app_name = 'lessons'
urlpatterns = [ 
path('<int:lesson_id>/', views.details_lesson, name='lessondet'),

]