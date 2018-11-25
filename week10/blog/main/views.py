from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IndexView(ListView):
	model = Post
	template_name = 'main/index.html'

	def get_queryset(self):
		if not self.request.user.is_anonymous:
			return Post.objects.for_author(self.request.user)
		else: 
			return Post.objects.all()

class PostDetailView(DetailView):
	model = Post
	template_name = 'main/detail.html'

class PostCreateView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'main/post_add_form.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)

class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'main/post_add_form.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		if not self.request.user.is_anonymous:
			self.object.user = self.request.user
		self.object.post = get_object_or_404(Post, pk=self.kwargs['pk'])
		self.object.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('detail', args=[self.kwargs['pk']])
