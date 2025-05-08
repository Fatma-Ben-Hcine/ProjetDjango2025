from django.db import models
from qcm.models import Qcm

class Question(models.Model):
    idQuestion = models.AutoField(primary_key=True)
    qcm = models.ForeignKey(Qcm, on_delete=models.CASCADE, related_name='questions')
    texte = models.TextField()

    def __str__(self):
        return self.texte

