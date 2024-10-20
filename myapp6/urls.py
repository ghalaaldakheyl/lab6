from django.urls import path
from .views import index, students_view, courses_view, details_view

urlpatterns = [
    path('', index, name='index'),
    path('students/', students_view, name='students'),
    path('courses/', courses_view, name='courses'),
    path('students/<int:student_id>/', details_view, name='details'),
]
