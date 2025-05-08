from django.shortcuts import render,get_object_or_404
from cours.models import Cours
from lesson.models import Lesson

def listeCours(request):
    cours=Cours.objects.all()
    return render(request, 'courses.html', {'cours': cours})

def details_cours(request, cours_id):
    cours = get_object_or_404(Cours, pk=cours_id)
    lessons = cours.lessons.all()  
    return render(request, 'details.html', {'cours': cours,'lessons': lessons})