from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Experience, Skill, Education, Profile
from .forms import experienceForm, educationForm, skillsForm, ContactForm

# Create your views here.

def home_view(request):
    
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    profiles = Profile.objects.all()
    
    
    context = {'experiences': experiences, 'skills': skills, 'educations':educations, 'profiles': profiles}
    return render(request, 'base/home.html', context)

def addExperience(request):
    
    form = experienceForm()
    
    if request.method == "POST":
        experienceAdd = experienceForm(request.POST)
        if experienceAdd.is_valid():
            experienceAdd.save()
            messages.success(request, 'Your experience details have been added')
            return redirect('home')
        
        
    
    return render(request, 'base/add.html', {'form':form})

def addEducation(request):
    
    form = educationForm()
    
    if request.method == "POST":
        educationAdd = educationForm(request.POST)
        if educationAdd.is_valid():
            educationAdd.save()
            messages.success(request, 'Your education details have been added')
            return redirect('home')
        
        
    
    return render(request, 'base/add.html', {'form':form})

def addSkills(request):
    form = skillsForm
    
    if request.method == "POST":
        skillAdd = skillsForm(request.POST)
        if skillAdd.is_valid():
            skillAdd.save()
            messages.success(request, 'Your skills have been added')
            return redirect('home')
    
        
    return render(request, 'base/add.html', {'form':form})

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['evanswandz@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "base/email.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message, I will get back to you as soon as possible')