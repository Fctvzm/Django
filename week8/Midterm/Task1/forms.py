from django import forms
from .models import Restaurant, Dish, Review
import datetime

class RestaurantForm(forms.ModelForm):

	class Meta:
		model = Restaurant
		fields = ['name', 'number', 'telephone', 'city']

class DishForm(forms.ModelForm):

	class Meta:
		model = Dish
		fields = ['name', 'description', 'price', 'restaurant']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = "__all__"