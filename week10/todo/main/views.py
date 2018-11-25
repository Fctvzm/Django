from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, TaskChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IndexView(ListView):
	model = Task
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['button_type'] = 'completed'
		return context

	def get_queryset(self):
		if not self.request.user.is_anonymous:
			return Task.objects.for_user(self.request.user)
		else:
			return Task.objects.all()

class CompletedListView(ListView):
	model = Task
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['button_type'] = 'incomplete'
		return context

	def get_queryset(self):
		if not self.request.user.is_anonymous:
			return Task.objects.for_user(self.request.user).filter(status = 'T')
		else:
			Task.objects.filter(status = 'T')

class TaskCreateView(CreateView):
	model = Task
	form_class = TaskForm
	template_name = 'main/add.html'
	success_url = reverse_lazy('main:index')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.owner = self.request.user
		self.object.dueon_date = form.cleaned_data['dueon_date']
		self.object.save()
		return super().form_valid(form)

class TaskUpdateView(UpdateView):
	model = Task
	form_class = TaskChangeForm
	success_url = reverse_lazy('main:index')
	template_name = 'main/change.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.dueon_date = form.cleaned_data['dueon_date']
		self.object.save()
		return super().form_valid(form)	

class TaskDeleteView(DeleteView):
	model = Task
	success_url = reverse_lazy('main:index')
	template_name = 'main/delete.html'

