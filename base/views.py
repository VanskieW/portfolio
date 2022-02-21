from django.shortcuts import render
from .models import Experience, Skill

# Create your views here.

def home_view(request):
    
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    
    
    
    context = {'experiences': experiences, 'skills': skills}
    return render(request, 'home.html', context)