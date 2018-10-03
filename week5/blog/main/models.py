from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 200)
	created_date = models.DateField('date published', auto_now = True)
	main_text = models.CharField(max_length = 1000)
	author = models.CharField(max_length = 100)

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.CharField(max_length = 100)
	content = models.CharField(max_length = 500)
	rating = models.IntegerField()
	post = models.ForeignKey('Post', on_delete = models.CASCADE)