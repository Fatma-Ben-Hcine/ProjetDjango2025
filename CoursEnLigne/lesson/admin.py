from django.contrib import admin
from lesson.models import Lesson
class LessonAdmin(admin.ModelAdmin):
    list_display=('cours','titrLesson','contenuLesson','niveau','estTermine')
list_per_page = 10
admin.site.register(Lesson,LessonAdmin)
