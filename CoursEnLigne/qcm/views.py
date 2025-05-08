from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from qcm.models import Qcm
from reponse.models import Reponse
from progres.models import ProgresUtilisateur

@login_required
def afficher_qcm(request, qcm_id):
    """Affiche le QCM avec toutes ses questions/réponses"""
    qcm = get_object_or_404(Qcm, pk=qcm_id)
    questions = qcm.questions.all()  
    
   
    bonnes_reponses = {str(q.idReponse) for q in questions if q.natureRep}
    
    return render(request, 'qcm.html', {
        'qcm': qcm,
        'questions': questions,
        'bonnes_reponses': bonnes_reponses  
    })

@login_required
def soumettre_qcm(request, qcm_id):
    if request.method == 'POST':
        qcm = get_object_or_404(Qcm, pk=qcm_id)
        questions = qcm.questions.all()
        score = 0
        total_questions = questions.count()

        for question in questions:
            if question.natureRep:
                if request.POST.get(f'question_{question.idReponse}') == 'on':
                    score += 1

        reussi = score >= qcm.scoreMax

        return render(request, 'resultats.html', {
            'score': score,
            'score_max': qcm.scoreMax,
            'total_questions': total_questions,
            'reussi': reussi,
            'lesson': qcm.lesson  # Ajout crucial
        })