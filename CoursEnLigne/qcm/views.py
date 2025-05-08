from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from qcm.models import Qcm
from question.models import Question
from reponse.models import Reponse

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

        return render(request, 'resultats.html', {
            'score': score,
            'score_max': qcm.scoreMax,
            'total_questions': questions.count(),
            'reussi': reussi,
            'lesson': qcm.lesson
        })