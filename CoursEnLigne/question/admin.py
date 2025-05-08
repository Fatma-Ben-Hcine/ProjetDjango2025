from django.contrib import admin
from question.models import Question
class QuestionAdmin(admin.ModelAdmin):
    list_display=('qcm','texte')
list_per_page = 10
admin.site.register(Question,QuestionAdmin)