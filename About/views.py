from django.shortcuts import render
from.models import*
from Club.models import*
from django.core.mail import send_mail,EmailMessage
import threading
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
# To MAKE EASIER FOR EMAILING A USER
#class EmailThread(threading.Thread):

   # def __init__(self, data):
        #self.data = data
        #threading.Thread.__init__(self)

    #def run(self):
        #self.data.send(data['subject'],message,'',['jonathanlibesa@gmail.com'])
        #self.email.send(fail_silently=False)



def About_zetech(request):
	abouts=About.objects.all()
	cat_menu=Club.objects.all()
	if request.method == "POST":
		name= request.POST['name']
		subject= request.POST['subject']
		email= request.POST['email']
		message= request.POST['message']

		data= {
			'name':name,
			'subject':subject,
			'email':email,
			'message':message
		}


		message= '''
		New message:{}

		from:{}
		'''.format(data['message'],data['email'])
		send_mail(data['subject'],message,'',['jonathanlibesa@gmail.com'])	
		messages.success(request,'We have recieved your email our team will respond to you soon')
		return render(request,'About/about_us.html')
	else:

		context={'abouts':abouts,'cat_menu':cat_menu}
		return render(request,'About/about_us.html',context)