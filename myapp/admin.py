from django.contrib import admin
from .models import Project, Task

# Register your models here.

#una ves agregado aqui, aparecera en admin
admin.site.register(Project)
admin.site.register(Task)