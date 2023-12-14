# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = "Django Course!!"
    return render(request,"index.html", {
        'title': title
    })

def about(request):
    username = 'Vladimir'       
    return render(request, "about.html", {
        'username': username
    })

def hello(request, id):
    result = id + 100 * 2
    return HttpResponse("<h2 >Hello %s</h2>" % result)

def landing(request, username):
    print(username)
    return HttpResponse("<h3> %s Brooo </h3>"% username)

def projects(request):
    # Convertimos el objeto en lista para luego serializarlo con Json y enviarlo al front
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)

    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # la linea de abajo sirve, pero el or_404 maneja el error de tarea no encontrada
    # task = Task.objects.get(id=id)
    # task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, title=title)
    # return HttpResponse('task: %s' % task.title)
    tasks = Task.objects.all()

    return render(request, "tasks.html", {
        'tasks':tasks
    })

def create_task(request):
    print(request.GET)
    if request.method == 'GET':
        return render(request, 'create_task.html',{
        'form': CreateNewTask()
    })
    else:
        # print(request.GET['title'])
        # print(request.GET['description'])

        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)

        return redirect('tasks/')
    
def path_test(request):
    return render(request, "path_test.html")