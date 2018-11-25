from django import forms
from .models import Task
import datetime

class TaskForm(forms.ModelForm):
	def clean_dueon_date(self):
		data = self.cleaned_data['dueon_date']
		if data < datetime.date.today():
			raise forms.ValidationError(('Invalid date - deadline time in past'))
		return data

	class Meta:
		model = Task
		fields = ['task_name', 'dueon_date', 'owner']
		labels = {'dueon_date': ('Deadline')}
		help_texts = {'dueon_date': ('Enter a date between now and future, not past time. Date formats: YYYY-MM-DD, MM/DD/YYYY, MM/DD/YY')}

class TaskChangeForm(forms.ModelForm):
	def clean_dueon_date(self):
		data = self.cleaned_data['dueon_date']
		if data < datetime.date.today():
			raise forms.ValidationError(('Invalid date - deadline time in past'))
		return data
		
	class Meta:
		model = Task
		fields = ['dueon_date', 'status']
		labels = {'dueon_date': ('Deadline')}
		help_texts = {'dueon_date': ('Enter a date between now and future, not past time. Date formats: YYYY-MM-DD, MM/DD/YYYY, MM/DD/YY')}
