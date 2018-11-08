from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Restaurant(models.Model):
	name = models.CharField(max_length = 100)
	number = models.IntegerField()
	telephone = models.IntegerField()
	city = models.CharField(max_length = 100)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return reverse('res_detail', args=[str(self.id)])

	def __str__(self):
		return self.name

class Dish(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	price = models.IntegerField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)

	def get_absolute_url(self):
		return reverse('dish_detail', args=[str(self.id)])

	def __str__(self):
		return self.name

class Review(models.Model):
	rating = models.IntegerField()
	comment = models.CharField(max_length = 200)
	date = models.DateField('date added', auto_now = True)

class RestaurantReview(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
	review = models.ForeignKey(Review, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

class DishReview(models.Model):
	dish = models.ForeignKey(Dish, on_delete = models.CASCADE)
	review = models.ForeignKey(Review, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)

