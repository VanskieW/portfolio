from django.forms import ModelForm

from .models import Experience, Skill, Education
from django import forms

class experienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'start_date', 'end_date', 'roles']
        
# Logic for raising error if end_date < start_date
    # def clean(self):
    #     cleaned_data = super().clean()
    #     start_date = cleaned_data.get("start_date")
    #     end_date = cleaned_data.get("end_date")
    #     if end_date < start_date:
    #         raise forms.ValidationError("End date should be greater than start date.")
    
class educationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['qualification', 'institution', 'start_date', 'end_date', 'grade']
        
class skillsForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        
class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
        