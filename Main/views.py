from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Users.decorators import allowed_users
from django.contrib.auth.models import Group
from.models import*
from Club.models import*
# Create your views here.




#TO DISPLAY THE HOME PAGE AND THE TEAM OF ZETECH

def home(request):
	team=Zetechteam.objects.all()
	page=Page.objects.all()
	cat_menu=Club.objects.all()
	video=Youtube.objects.all()
	context={'team':team,'page':page,'cat_menu':cat_menu,'video':video}
	return render(request,'main/home.html',context)



#TO DISPLAY THE DASHBOARD FOR THE SITE
@login_required(login_url='login')
@allowed_users(allowed_roles=['User','Admin'])
def user(request):
	cat_menu=Club.objects.all()
	context={'cat_menu':cat_menu}
	return render(request,'main/user.html',context)


#TO HANDLE ERROR IN THE SITE
def handle_not_found(request,exception):
	return render(request,'main/not found.html')


#TO HANDLE SERVER ERROR
def handle_server_error(request):
	return render(request,'main/server-error.html')