from django.shortcuts import render,get_object_or_404
from cours.models import Cours
from progres.models import ProgresUtilisateur

def listeCours(request):
    cours=Cours.objects.all()
    return render(request, 'courses.html', {'cours': cours})


def details_cours(request, cours_id):
    cours = get_object_or_404(Cours, pk=cours_id)
    lessons = cours.lessons.all()

    # Récupérer le niveau de l'utilisateur pour chaque leçon
    niveau_utilisateur = {}
    for lesson in lessons:
        # Chercher le progrès de l'utilisateur pour chaque leçon
        progres = ProgresUtilisateur.objects.filter(user=request.user, lesson=lesson).first()
        if progres:
            niveau_utilisateur[lesson.idLesson] = progres.niveau
        else:
            niveau_utilisateur[lesson.idLesson] = 0  # Si l'utilisateur n'a pas de progression, niveau par défaut à 0

    return render(request, 'details.html', {'cours': cours, 'lessons': lessons, 'niveau_utilisateur': niveau_utilisateur})
