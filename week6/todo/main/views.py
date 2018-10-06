from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, TaskChangeForm

def index(request):
	task_list = Task.objects.all()
	return render(request, 'index.html', {'task_list': task_list, 'button_type': 'completed'})

def completed(request):
	completed_list = Task.objects.filter(status = 'T')
	return render(request, 'index.html', {'task_list': completed_list, 'button_type': 'incomplete'})

def add(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit = False)
			task.dueon_date = form.cleaned_data['dueon_date']
			task.save()
			return redirect('index')
	else:
		form = TaskForm()
	return render(request, 'main/add.html', {'form': form})

def delete(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	task.delete()
	return redirect('index')

def change(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	if request.method == "POST":
		form = TaskChangeForm(request.POST, instance=task)
		if form.is_valid():
			task = form.save(commit = False)
			task.dueon_date = form.cleaned_data['dueon_date']
			task.save()
			return redirect('index')
	else:
		form = TaskChangeForm(instance=task)
	return render(request, 'main/add.html', {'form': form, 'task_name': task.task_name})
