from django.db import models
from django.contrib.auth.models import User
from lesson.views import Lesson

class ProgresUtilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    niveau= models.IntegerField(default=0)
    date_completed = models.DateTimeField(null=True, blank=True)
