from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm

def index(request):
    return render(request, 'myapp6/index.html')

def students_view(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    return render(request, 'myapp6/students.html', {'students': students, 'form': form})

def courses_view(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()

    return render(request, 'myapp6/courses.html', {'courses': courses, 'form': form})

def details_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    not_registered_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = get_object_or_404(Course, pk=course_id)
        student.courses.add(course)
        return redirect('details', student_id=student.id)

    return render(request, 'myapp6/details.html', {
        'student': student,
        'not_registered_courses': not_registered_courses,
    })
