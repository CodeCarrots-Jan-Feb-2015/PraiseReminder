from django.shortcuts import render, redirect
from django.http import HttpResponse
from backend.forms import PraiseForm
from backend.models import Praise 
import random
from django.views.generic.edit import UpdateView

def home(request):
	if request.user.is_authenticated ():
	
		praise = random.choice(Praise.objects.filter(user=request.user))
   		return render (request, "home.html",{'praise': praise})

   	else:
   		return redirect ("/admin/login/?next=/")
#delete a praise
def delete(request, praise_id):    
	praise = Praise.objects.get(id=praise_id)
	praise.delete()
	return render(request, "delete.html", {'praise': praise})

#edit a praise
def edit(request, praise_id):	
	praise = Praise.objects.get(id=praise_id)
	#process form data is a 'POST'
	#show a form is 'GET'
	if request.method == 'POST':
		form = PraiseForm(request.POST,instance=praise)

		if form.is_valid():
			#save the new category to the database.
			form.save()
			#user will be shown the homepage
			return redirect ("/")
		else:
			#prints that the form was not pushed
			print form.errors
	else: #If the request was not a POST, the form will display
		form = PraiseForm(instance=praise)
	return render(request, "edit.html", {'form':form})


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
			return redirect ("/")

		else:
			#prints that the form was not pushed
			print form.errors
	else: #If the request was not a POST, the form will display
		form = PraiseForm

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request, 'add.html', {'form':form})



# Create your views here.
