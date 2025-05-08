from django.shortcuts import render,get_object_or_404
from lesson.models import Lesson

def details_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    qcms = lesson.qcm.all()  
    return render(request, 'lesson.html', {'lesson': lesson,'qcms': qcms})