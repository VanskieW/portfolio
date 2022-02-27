from django.urls import path 
from django.conf.urls import url
from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('add-experience/', views.addExperience, name='add-experience'),
    path('add-education/', views.addEducation, name='add-education'),
    path('add-skills/', views.addSkills, name='add-skills'),
    

    path(r'^email/$', views.email, name='email'),
    path(r'^thanks/$',views.thanks, name='thanks'),

    
    
    
    
    
    
]
