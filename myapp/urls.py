from django.urls import path

#configuramos las vistas(views) de la app
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<int:id>', views.hello, name="hello"),
    path('hellolanding/<str:username>', views.landing, name="hello_to"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task', views.create_task, name="create_task"),
    path('create_project', views.create_project, name="create_project"),
    path('path_test', views.path_test)
]