from django.db import models
from django.contrib.auth.models import User

class Advert(models.Model):
	title = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	description = models.CharField(max_length = 300)
	price = models.IntegerField()
	number_of_views = models.IntegerField()
	owner = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title


