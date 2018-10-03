from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def index(request):
	post_list = Post.objects.all()
	return render(request, 'main/index.html', {'post_list': post_list})

def detail(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	comments = post.comment_set.all()
	return render(request, 'main/detail.html', {'post': post, 'comments': comments})

