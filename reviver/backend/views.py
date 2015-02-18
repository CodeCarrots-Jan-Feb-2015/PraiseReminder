from django.shortcuts import render
from django.http import HttpResponse
from backend.forms import PraiseForm
from backend.models import Praise 
import random

def home(request):
	praise = random.choice(Praise.objects.filter(user=request.user))
   	return render (request, "home.html",{'praise':praise})

def delete(request):
    return render (request, "delete.html")

def edit(request):
    return render (request, "edit.html")

def add(request):

	#process form data is a 'POST'
	#show a form is 'GET'
	if request.method == 'POST':
		form = PraiseForm(request.POST)

		if form.is_valid():
			#save the new category to the database.
			praise = form.save(commit=False)
			praise.user = request.user
			praise.save()


			#user will be shown the homepage
			return home(request)

		else:
			#prints that the form was not pushed
			print form.errors
	else: #If the request was not a POST, the form will display
		form = PraiseForm

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request, 'add.html', {'form':form})



# Create your views here.
