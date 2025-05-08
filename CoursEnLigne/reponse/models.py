from django.db import models
from question.models import Question

class Reponse(models.Model):
    idReponse = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponses')
    rep = models.TextField()
    natureRep = models.BooleanField()  # True si c’est une bonne réponse

    def __str__(self):
        return self.rep
