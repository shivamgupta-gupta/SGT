from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student
def index(request):
	a=Student.objects.all()
	context={'students':a}
	return render(request,'students/students.html',context)
	

















