from django.db import models

class Cours(models.Model):
    idCours = models.AutoField(primary_key=True)
    titreCours=models.CharField(max_length=20)
    descriptionCours=models.TextField()
    imageCours=models.CharField(max_length=250)
    nombreNiveau=models.IntegerField(null=True)

    def __str__(self):
        return self.titreCours


