from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class PostManager(models.Manager):
	def for_author(self, author):
		return self.filter(author=author)

class Post(models.Model):
	title = models.CharField(max_length = 200)
	created_date = models.DateField('date published', auto_now = True)
	main_text = models.CharField(max_length = 1000)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	objects = PostManager()
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])

	def to_json(self):
		return {
            'id': self.pk,
            'title': self.title,
            'author': self.author.username,
			'main_text': self.main_text,
		}

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
	content = models.CharField(max_length = 500)
	rating = models.IntegerField()
	post = models.ForeignKey('Post', on_delete = models.CASCADE)

	def to_json(self):
		return {
            'id': self.pk,
            'content': self.content,
			'rating': self.rating,
		}