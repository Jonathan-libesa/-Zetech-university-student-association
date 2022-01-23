from django.shortcuts import render
from.models import*
# Create your views here.
def aboutZusa(request):
	abouts=About.objects.all()
	context={'abouts':abouts}
	return render(request,'About/about.html',context)