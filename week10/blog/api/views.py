from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from main.models import Post, Comment

@csrf_exempt
def post_list(request):
	if request.method == 'GET':
		posts = Post.objects.all()
		posts = [p.to_json() for p in posts]
		return JsonResponse(posts, safe=False)
	elif request.method == 'POST':
		data = json.loads(request.body)
		post = Post(title = data['title'], main_text = data['main_text'], author = User.objects.first())
		post.save()
		return JsonResponse(post.to_json())

@csrf_exempt
def post_detail(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Exception as e:
		return JsonResponse({'error': str(e)}, status=404)

	if request.method == 'GET':
		return JsonResponse(post.to_json())

	elif request.method == 'PUT':
		data = json.loads(request.body)
		post.title = data.get('title', post.title)
		post.main_text = data.get('main_text', post.main_text)
		post.author = request.user
		post.save()
		return JsonResponse(post.to_json())
	elif request.method == 'DELETE':
		student.delete()
		return JsonResponse({'deletetd': True}, status=204)

@csrf_exempt
def comment(request, pk):
	try:
		post = Post.objects.get(pk=pk)
	except Exception as e:
		return JsonResponse({'error': str(e)}, status=404)

	if request.method == 'GET':
		comments = [obj.to_json() for obj in post.comment_set.all()]
		return JsonResponse(comments, safe=False)

	elif request.method == 'POST':
		data = json.loads(request.body)
		comment = Comment(user=User.objects.first(), content=data['content'], rating=data['rating'], post=post)
		comment.save()
		return JsonResponse(comment.to_json())
