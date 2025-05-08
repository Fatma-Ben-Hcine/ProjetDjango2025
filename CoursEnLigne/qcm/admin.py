from django.contrib import admin
from qcm.models import Qcm
class QcmAdmin(admin.ModelAdmin):
    list_display=('lesson','titreQcm','scoreMax')
list_per_page = 10
admin.site.register(Qcm,QcmAdmin)
