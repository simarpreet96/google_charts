from django.shortcuts import render,redirect
import math
from django.contrib.auth.decorators import login_required
from .models import Circle


def home(request):
	return render(request, 'charts/index.html')

def circle_add(request):
	radius1=float(request.POST['radius'])
	area=float(3.14*radius1*radius1)
	circumf=float(2*3.14*radius1)

	return render(request,'charts/index.html',{'area':area, 'circumf':circumf})




