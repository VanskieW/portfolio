from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField(blank=False)
    end_date = models.DateField()
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
    
    
        
    
