from django.shortcuts import render, redirect
from .models import Student, Pulpit1, Leaders1, Reviewers, Project
from .forms import FindGroup, FindProj, FindStud, FindLid, FindRev


def index(request):
    student2 = Student.objects.all()

    context = {

        'student2': student2
    }

    return render(request, 'main/index.html', context)
