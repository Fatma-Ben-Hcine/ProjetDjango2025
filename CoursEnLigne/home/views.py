from django.shortcuts import render 
from cours.models import Cours
def index(request):
    cours=Cours.objects.all()
    return render(request, 'index.html', {'cours': cours})