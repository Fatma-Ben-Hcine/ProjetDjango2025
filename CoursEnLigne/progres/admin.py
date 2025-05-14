from django.contrib import admin
from .models import ProgresUtilisateur

class ProgresUtilisateurAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'score', 'niveau', 'date_completed')

admin.site.register(ProgresUtilisateur, ProgresUtilisateurAdmin)
