from django.shortcuts import render
from.models import*
from Club.models import*
# Create your views here.
def About_zetech(request):
	abouts=About.objects.all()
	cat_menu=Club.objects.all()
	context={'abouts':abouts,'cat_menu':cat_menu}
	return render(request,'About/about.html',context)