from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
	post_list = Post.objects.all()
	return render(request, 'main/index.html', {'post_list': post_list})

def detail(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	comments = post.comment_set.all()
	return render(request, 'main/detail.html', {'post': post, 'comments': comments})

def addPost(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request, 'main/add.html', {'form': form, 'comment': False})

def addComment(request, post_id):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			if not request.user.is_anonymous:
				comment.user = request.user
			post = get_object_or_404(Post, pk = post_id)
			comment.post = post
			comment.save()
			return redirect('detail', post_id = post_id)
	else:
		form = CommentForm()
	return render(request, 'main/add.html', {'form': form, 'comment': True})
