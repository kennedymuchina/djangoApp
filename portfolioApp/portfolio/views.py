from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.filter().order_by('-finished_date')
    return render(request, 'portfolio/index.html', {'projects' : projects})
