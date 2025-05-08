from django.db import models
from qcm.models import Qcm
class Reponse(models.Model):
    idReponse=models.AutoField(primary_key=True)
    qcm=models.ForeignKey(Qcm,on_delete=models.CASCADE,related_name='questions')
    rep=models.CharField(max_length=10)
    natureRep=models.BooleanField()
    
    def __str__(self):
        return self.rep