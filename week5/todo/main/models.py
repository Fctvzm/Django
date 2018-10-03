from django.db import models

class Task(models.Model):
	task_name = models.CharField(max_length = 200)
	created_date = models.DateField('date published', auto_now = True)
	dueon_date = models.DateField('date deadline')
	STATUS_CHOICES = (
		('T', 'Done'),
		('F', 'Not Done')
	)
	status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'F')
	owner = models.CharField(max_length = 10)

	def __str__(self):
		return self.task_name

