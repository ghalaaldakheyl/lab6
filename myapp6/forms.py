from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'courses']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']