from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import DetailView,ListView
from.models import*
from django.contrib.auth.decorators import login_required
from.forms import ClubForm,EventForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.core import serializers
from django.template.loader import render_to_string
# Create your views here


#TO SHOW THE CLUBS IN THE SCHOOL AND SEARCH FOR THE CLUB
@login_required(login_url='login')
def clubs(request):
	#search engine
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			clubs=Club.objects.filter(
				Q( Name__icontains=query)
			)
		else:
			clubs=Club.objects.all()
	paginator=Paginator(clubs,per_page=7)
	page_number=request.GET.get('page',1)
	clubs_obj=paginator.get_page(page_number)

	context={'clubs':clubs_obj,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'main/clubuser.html',context)


#TO SHOW DETAILS OF THE CLUB AND PARTICIPANTS
@login_required(login_url='login')
def Clubdetails(request,pk):
	career=get_object_or_404(Club,id=pk)
	#career=Club.objects.get(id=pk)
	participants=career.participants.all()
	number_of_participants=len(participants)
	if len(participants) == 0:
		is_following = False
	for participant in participants:
		if participant == request.user:
			is_following = True
			break
		else:
			is_following = False
	context={'career':career,'number_of_participants':number_of_participants,'is_following':is_following,'participants':participants}
	return render(request,'main/detail.html',context)




#TO SHOW EACH CLUB EVENT ON THE CLUB 
@login_required(login_url='login')	
def Clubevent(request,club):
	events=Event.objects.filter(Club_Name=club)
	paginator=Paginator(events,per_page=2)
	page_number=request.GET.get('page',1)
	events_obj=paginator.get_page(page_number)
	context={'events':events_obj,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'main/club_events.html',context)



#TO ADD PARTICIPANTS TO JION GROUP
@login_required(login_url='login')	
def addparticipants(request,pk):
	career=get_object_or_404(Club,id=pk)
	career.participants.add(request.user)
	messages.success(request,"You have Jioned Sucessfully")
	return redirect('details',pk=career.pk)


#TO REMOVE PARTICIPANT TO JION GROUP
@login_required(login_url='login')
def removeparticipants(request,pk):
	career=get_object_or_404(Club,id=pk)
	career.participants.remove(request.user)
	messages.warning(request,'You have Left the Club Sucessfully')
	return redirect('details',pk=career.pk)


#TO EDIT THE CLUB  INFORMATION ADMIN
@login_required(login_url='login')
def Editclub(request,pk):
	career=get_object_or_404(Club,id=pk)
	form=ClubForm(instance=career)
	if request.method == "POST":
		form=ClubForm(request.POST,request.FILES,instance=career)
		if form.is_valid():
			form.save()
		messages.success(request, 'Club updated sucessfully')
		return redirect('details',pk=career.pk)
	context = {'form':form}	
	return render(request,'main/editclub.html',context)


 #TO SHOW CREATE EVENT OF THE CLUB ADMIN
@login_required(login_url='login')
def createEvent(request,pk):
	Club_Name=get_object_or_404(Club,id=pk)
	career=get_object_or_404(Club,id=pk)
	Club_Name=Club_Name
	form=EventForm(initial={'Club_Name':Club_Name})
	if request.method == 'POST':
		form=EventForm(request.POST,request.FILES,Club_Name)
		if form.is_valid():
			Event=form.save(commit=False)
			Event.manager=request.user
			Event.Club_Name=Club_Name
			Event.save()
		#messages.add_message(request,messages.success,'CLUB EVENT ADDED SUCESSFULLY')
		return redirect('details',pk=career.pk)
	context={'form':form}
	return render(request, 'main/create event.html',context)

#TO EDIT EVENT OF THE CLUB ADMIN
@login_required(login_url='login')
def EditEvent(request,pk):
	event=get_object_or_404(Event,id=pk)
	form=EventForm(instance=event)
	if request.method == 'POST':
		form=EventForm(request.POST,request.FILES,instance=event)
		if form.is_valid():
			form.save()
			messages.success(request,'CLUB EVENT EDITTED SUCESSFULLY')
		return redirect('clubuser')
	context={'form':form}
	return render(request,'main/create event.html',context)



#TO DELETE THE EVENT OF A CLUB 
@login_required(login_url='login')
def DeleteEvent(request,pk):
	event=get_object_or_404( Event,id=pk)
	if event.Photo_Video:
		event.Photo_Video.delete()
	event.delete()
	messages.warning(request,'CLUB EVENT WAS DELETED SUCESSFULLY')	
	return redirect('clubuser')


#TO SHOW PARTICIPANTS OF THE GROUP TO CLUB ADMIN
@login_required(login_url='login')
def groupfollower(request,pk):
	career=get_object_or_404(Club,id=pk)
	participants=career.participants.all()
	number_of_participants=len(participants)
	if len(participants) == 0:
		is_following = False
	for participant in participants:
		if participant == request.user:
			is_following = True
			break
		else:
			is_following = False
	context={'number_of_participants':number_of_participants,'is_following':is_following,'participants':participants}
	return render(request,'main/Participants.html',context)


# Load More
def load_more(request):
	post=self.get_object()
	offset=int(request.POST['offset'])
	limit=2
	posts=Club.objects.all()[offset:limit+offset]
	totalData=Club.objects.all().count()
	data={}
	posts_json=serializers.serialize('json',posts)
	return JsonResponse(data={
		'posts':posts_json,
	    'totalResult':totalData
		})