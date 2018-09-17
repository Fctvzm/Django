from django.shortcuts import render, get_object_or_404
from .models import Task

def index(request):
	task_list = Task.objects.all()
	return render(request, 'main/index.html', {'task_list': task_list, 'button_type': 'completed'})

def detail(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	return render(request, 'main/detail.html', {'task': task})

def completed(request):
	completed_list = Task.objects.filter(status = 'T')
	return render(request, 'main/index.html', {'task_list': completed_list, 'button_type': 'incomplete'})
