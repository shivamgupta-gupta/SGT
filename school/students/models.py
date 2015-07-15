from django.db import models
# Create your models here.
class Student(models.Model):
	text=models.CharField(max_length=500)
	date=models.DateTimeField('date published')
	def __str__(self):
		return self.text
