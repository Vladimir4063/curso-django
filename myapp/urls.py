from django.urls import path

#configuramos las vistas(views) de la app
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:id>', views.hello),
    path('hellolanding/<str:username>', views.landing),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create_task', views.create_task),
    path('path_test', views.path_test)
]