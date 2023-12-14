from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    # Esta funcion(metodo al estar dentro de una clase) 
    # me permite devolver el titulo(str) al panel admin
    def __str__(self):
        return self.name 

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        # Esta concatenacion me permite ver a que proyecto
        # esta relacionada esa tarea
        return self.title + ' - ' + self.project.name