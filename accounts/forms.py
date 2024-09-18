from django import forms
from .models import Snippet
from django.utils import timezone
class SnippetForm(forms.ModelForm):
	class Meta:
		model=Snippet
		fields=('Name','Email','Source','Destination','Departure','Arrival')