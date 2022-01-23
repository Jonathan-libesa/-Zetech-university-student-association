from django import forms
from .models import* 
from Main.validators import validate_file_size,file_size
class CareerForm(forms.ModelForm):
	class Meta:
		model=Career
		fields='__all__'
		exclude=['author']

class ForumForm(forms.ModelForm):
	Photo_Video= forms.FileField(required=False, validators=[validate_file_size])
	class Meta:
		model=Forum
		fields=['title','description']
		exclude=['author']
class CommentForm(forms.ModelForm):
	content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control jqte','cols':"10",'rows':'1','Placeholder':'Say something ..'}))
	class Meta:
		model=Comment
		fields=['content']
		


