from django.contrib import admin
from .models import ProgresUtilisateur

class ProgresUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'estCompleted', 'score', 'niveau', 'date_completed')
    list_filter = ('estCompleted', 'niveau')
    search_fields = ('user__username', 'lesson__titrLesson')

admin.site.register(ProgresUtilisateur, ProgresUtilisateurAdmin)
