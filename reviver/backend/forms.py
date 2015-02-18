##forms.py is meant to store form-related classes

from django import forms
from backend.models import Praise

class PraiseForm(forms.ModelForm):
	class Meta:
		#provides an association between the model form and a model
		model = Praise
		exclude = ['user']
