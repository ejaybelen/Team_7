from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_syllabus, name='list-syllabus'),
    path('add_syllabus', views.add_syllabus, name='add-syllabus'),
    path('show_syllabus/<syllabus_id>', views.show_syllabus, name='show-syllabus'),
    path('search_syllabus', views.search_syllabus, name='search-syllabus'),
    path('update_syllabus/<syllabus_id>', views.update_syllabus, name='update-syllabus'),
    path('delete_syllabus/<syllabus_id>', views.delete_syllabus, name='delete-syllabus'),
    path('course_pdf/<syllabus_id>', views.course_pdf, name='course-pdf'),
]
