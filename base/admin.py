from django.contrib import admin
from .models import Experience, Skill,Education, Profile

# Register your models here.

admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Profile)