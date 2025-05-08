from django.db import models
from lesson.models import Lesson
class Qcm(models.Model):
    idQcm=models.AutoField(primary_key=True)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='qcm')
    titreQcm=models.TextField()
    scoreMax=models.IntegerField(default=3, editable=False)

    def __str__(self):
        return self.titreQcm