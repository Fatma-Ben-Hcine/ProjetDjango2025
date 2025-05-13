from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from qcm.models import Qcm
from question.models import Question
from lesson.models import Lesson
from progres.models import ProgresUtilisateur

@login_required
def afficher_qcm(request, qcm_id):
    qcm = get_object_or_404(Qcm, pk=qcm_id)
    questions = qcm.questions.prefetch_related('reponses')

    return render(request, 'qcm.html', {
        'qcm': qcm,
        'questions': questions,
    })

@login_required
def soumettre_qcm(request, qcm_id):
    if request.method == 'POST':
        qcm = get_object_or_404(Qcm, pk=qcm_id)
        questions = qcm.questions.prefetch_related('reponses')
        score = 0

        for question in questions:
            bonnes_reps = set()
            for rep in question.reponses.filter(natureRep=True):
                bonnes_reps.add(str(rep.idReponse))
            reps_cochees = set(request.POST.getlist(f'question_{question.idQuestion}'))
            if bonnes_reps == reps_cochees:
                score += 1

        reussi = score >= qcm.scoreMax
        
        progres, created = ProgresUtilisateur.objects.get_or_create(
            user=request.user,
            lesson=qcm.lesson,
            defaults={
                'score': score,
                'estCompleted': reussi,
                'niveau': 1,  # Initialisation du niveau à 1 si c'est un nouveau progrès
            }
        )

        # Si l'entrée de progression existe déjà, mettre à jour le score et le niveau
        if not created:
            progres.score = max(progres.score, score)
            if reussi and not progres.estCompleted:
                progres.estCompleted = True
                progres.niveau += 1  # Incrémenter le niveau si le QCM est réussi
            progres.save()

        # Si l'utilisateur réussit le QCM, on récupère la leçon suivante
        if reussi:
            prochaine_lecon = Lesson.objects.filter(idLesson__gt=qcm.lesson.idLesson).order_by('idLesson').first()

            if prochaine_lecon:
                ProgresUtilisateur.objects.get_or_create(
                    user=request.user,
                    lesson=prochaine_lecon,
                    defaults={
                        'niveau': progres.niveau,  # On garde le niveau actuel pour la leçon suivante
                        'score': 0,
                        'estCompleted': False,
                    }
                )

        return render(request, 'resultats.html', {
            'score': score,
            'score_max': qcm.scoreMax,
            'total_questions': questions.count(),
            'reussi': reussi,
            'lesson': qcm.lesson,
            'niveau': progres.niveau  # Affichage du niveau dans le template
        })
