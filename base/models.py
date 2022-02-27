
from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    about = models.TextField()
    email = models.EmailField()
    telephone = models.PositiveIntegerField()
    
    def __str__(self):
        return self.full_name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True)
    roles = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-end_date']
    
class Skill(models.Model):
    name = models.CharField(max_length=200)
    proficiency = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    
class Education(models.Model):
    qualification = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField(blank=False)
    end_date = models.DateField()
    grade = models.CharField(max_length=30)
    
    def __str__(self):
        return self.qualification
    
    class Meta:
        ordering = ['-end_date']
    
