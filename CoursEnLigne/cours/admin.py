from django.contrib import admin
from cours.models import Cours
from django.utils.html import format_html
class CoursAdmin(admin.ModelAdmin):
    list_display=('titreCours','descriptionCours','image_preview','nombreNiveau')
    def image_preview(self,obj):
        if obj.imageCours:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.imageCours)
        return "Pas d'image"
    image_preview.short_description = "Image"
    list_per_page = 10
admin.site.register(Cours,CoursAdmin)
