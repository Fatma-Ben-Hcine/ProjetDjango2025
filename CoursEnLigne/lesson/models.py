from django.db import models
from cours.models import Cours

class Lesson(models.Model):
    idLesson=models.AutoField(primary_key=True)
    cours=models.ForeignKey(Cours,on_delete=models.CASCADE,related_name='lessons')
    titrLesson=models.CharField(max_length=10)
    contenuLesson=models.TextField()
    niveau=models.IntegerField()
    estTermine=models.BooleanField(default=False)

    def __str__(self):
        return self.titrLesson


