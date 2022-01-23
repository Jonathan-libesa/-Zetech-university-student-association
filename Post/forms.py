from django import forms
from .models import*
class CommentForm(forms.ModelForm):
	content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-10','rows':'5','Placeholder':'Say something ..'}))

	class Meta:
		model=Comment
		fields=( 'content',)