from django.contrib import admin
from reponse.models import Reponse
class ReponseAdmin(admin.ModelAdmin):
    list_display=('qcm','rep','natureRep')
list_per_page = 10
admin.site.register(Reponse,ReponseAdmin)
