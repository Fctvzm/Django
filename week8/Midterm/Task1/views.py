from django.urls import reverse_lazy
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class IndexView(ListView):
	model = Restaurant
	template_name = 'index.html'

class DishView(ListView):
	model = Dish
	template_name = 'Task1/dishes.html'

class ResDetailView(DetailView):
	model = Restaurant
	template_name = 'Task1/res_detail.html'

class ResCreateView(CreateView):
	model = Restaurant
	fields = ['name', 'number', 'telephone', 'city'] 
	template_name = 'Task1/res_add_form.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(ResCreateView, self).form_valid(form)

class ResUpdateView(UpdateView):
	model = Restaurant
	fields = ['name', 'number', 'telephone', 'city']
	template_name = 'Task1/res_update_form.html'

class ResDeleteView(DeleteView):
	model = Restaurant
	success_url = reverse_lazy('index')
	template_name = 'Task1/res_delete_form.html'
