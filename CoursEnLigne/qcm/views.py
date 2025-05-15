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
            bonne_rep = question.reponses.filter(natureRep=True).first()
            rep_cochee = request.POST.get(f'question_{question.idQuestion}')
            if bonne_rep and str(bonne_rep.idReponse) == rep_cochee:
                score += 1

        reussi = score >= qcm.scoreMax

        progres, created = ProgresUtilisateur.objects.get_or_create(
            user=request.user,
            lesson=qcm.lesson,
            defaults={'score': score}
        )

        if not created:
            progres.score = score

        if reussi and not qcm.lesson.estTermine:
            qcm.lesson.estTermine = True
            qcm.lesson.save()

        cours = qcm.lesson.cours
        cours_id = cours.idCours  

        lecons_du_cours = cours.lessons.all()

        lecons_achevees = ProgresUtilisateur.objects.filter(
            user=request.user,
            lesson__in=lecons_du_cours,
            lesson__estTermine=True
        ).count()

        progres.niveau = lecons_achevees
        progres.save()

        return render(request, 'resultats.html', {
            'score': score,
            'score_max': qcm.scoreMax,
            'total_questions': questions.count(),
            'reussi': reussi,
            'lesson': qcm.lesson,
            'cours_id': cours_id,
            'niveau': lecons_achevees
        })
