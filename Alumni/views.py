from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.core.paginator import Paginator
from.models import*
from.forms import CareerForm,ForumForm,CommentForm
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


# THE ALUMNI HOMEPAGE AND ANY UPCOMING EVENTS
@login_required(login_url='login')
def homepage(request):
	events=Event.objects.all()
	paginator=Paginator(events,per_page=1)
	page_number=request.GET.get('page',1)
	events_obj=paginator.get_page(page_number)
	context={'events':events_obj,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'main/home_alumni.html',context)


# TO LIST THE ALUMNI AND SEARCH
@login_required(login_url='login')
def alumnilist(request):
    #search engine
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            alumni=Alumni.objects.filter(
            	Q( Last_name__icontains=query) |
        		Q(first_name__icontains=query) 
            )
        else:
            alumni=Alumni.objects.all()

    context={'alumni':alumni}
    return render(request,'main/alumni_list.html',context)


# Detailview,delete and update of Job
@login_required(login_url='login')
def job_view(request,pk):
	career=get_object_or_404(Career,id=pk)
	#career=Career.objects.get(id=pk)
	form=CareerForm(instance=career)
		#UPDATE JOB
	if request.method == 'POST':
		form=CareerForm(request.POST,instance=career)
		if form.is_valid():
			form.save()
			return redirect('job_view',pk=career.id)
	if request.method == 'POST':
		career.delete()
		return redirect('job_list')
	context = {'obj':career,'career':career,'form':form}
	return render(request,'main/job_view.html',context)
#end of detailview


#TO CREATE JOB AND LIST THEM AND ALSO SERACH
@login_required(login_url='login')
def Job(request):
	#Create job function
	form=CareerForm()
	if request.method == 'POST':
		form=CareerForm(request.POST)
		if form.is_valid():
			career=form.save(commit=False)
			career.author=request.user
			career.save()
			return redirect('job_list')
    #Search engine
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			career=Career.objects.filter(
				Q(job_title__icontains=query)|
				Q(Description__icontains=query)

			)
		else:
			career=Career.objects.all()
	#paginator
	paginator=Paginator(career,per_page=2)
	page_number=request.GET.get('page',1)
	career_obj=paginator.get_page(page_number)
	context={'career':career_obj,'paginator':paginator,'page_number':int(page_number),'form':form}
	return render(request,'main/job_list.html',context)


#TO  CREATE FORUM AND LIST THEMA AND ALSO SERACH
@login_required(login_url='login')
def forum_create_list(request):
	#create job post function
	form=ForumForm()
	if request.method == 'POST':
		form=ForumForm(request.POST,request.FILES)
		if form.is_valid():
			forum=form.save(commit=False)
			forum.author=request.user
			forum.save()
			return redirect('forum')
   #search for forum 
	if request.method == 'GET':
		query=request.GET.get('query')
		if query:
			forum=Forum.objects.filter(
				Q(title__icontains=query)|
				Q(description__icontains=query)
			)
		else:
			forum=Forum.objects.all()
	#paginator
	paginator=Paginator(forum,per_page=3)
	page_number=request.GET.get('page',1)
	forum_obj=paginator.get_page(page_number)
	context={'forum':forum_obj,'form':form,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'main/forum.html',context)





# Delete  Forum
@login_required(login_url='login')
def delete(request, pk):
	forum=get_object_or_404(Forum,id=pk)
	if request.method == 'POST':
		forum.delete()
		return HttpResponseRedirect(reverse('forum'))
	context={'forum':forum}
	return render(request,'main/delete_forum.html',context)




