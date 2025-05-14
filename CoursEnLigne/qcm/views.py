from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from qcm.models import Qcm
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
            bonnes_reps = set(str(rep.idReponse) for rep in question.reponses.filter(natureRep=True))
            reps_cochees = set(request.POST.getlist(f'question_{question.idQuestion}'))
            if bonnes_reps == reps_cochees:
                score += 1

        reussi = score >= qcm.scoreMax

        # Mise à jour ou création de la progression de l'utilisateur
        progres, created = ProgresUtilisateur.objects.update_or_create(
            user=request.user,
            lesson=qcm.lesson,
            defaults={
                'score': score,
                # 'niveau' peut être modifié ici si nécessaire
            }
        )

        # Marquer la leçon comme terminée si le QCM est réussi
        if reussi:
            qcm.lesson.estTermine = True
            qcm.lesson.save()

            # Met à jour le niveau de l'utilisateur basé sur les leçons complétées
            lecons_completees = ProgresUtilisateur.objects.filter(
                user=request.user,
                lesson__estTermine=True  # Assure-toi que les leçons terminées sont prises en compte
            ).order_by('date_completed')

            for index, progression in enumerate(lecons_completees, start=1):
                progression.niveau = index
                progression.save()

            niveau = lecons_completees.count()
        else:
            niveau = progres.niveau if hasattr(progres, 'niveau') else 0

        return render(request, 'resultats.html', {
            'score': score,
            'score_max': qcm.scoreMax,
            'total_questions': questions.count(),
            'reussi': reussi,
            'lesson': qcm.lesson,
            'niveau': niveau
        })
