from django import forms
from .models import Property


class SearchForm(forms.Form):
	Region = forms.CharField()
	Bedroom = forms.CharField()
	Bathroom = forms.CharField()
	LowerPrice = forms.CharField()
	UpperPrice = forms.CharField()
	ConvenientPoint = forms.CharField()

class PInfoForm(forms.ModelForm):
	class Meta:
		model = Property

