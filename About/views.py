from django.shortcuts import render
from.models import*
# Create your views here.
def About_zetech(request):
	abouts=About.objects.all()
	context={'abouts':abouts}
	return render(request,'About/about.html',context)