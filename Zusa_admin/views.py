from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from Users.models import*
from News.models import*
from About.models import*
from Club.models import*
from Post.models import*
from Leaders.models import*
from Alumni.models import *
from Student.models import*
from Main.models import*
from django.core.paginator import Paginator
from.forms import*
from poll .models import *
from Users.decorators import allowed_users,admin_only

@login_required(login_url='login')
@admin_only
def admin_dashboard_view(request):
    dict={
        'total_user':User.objects.all().count(),
        'total_News':Announcement.objects.all().count(),
        'total_Club':Club.objects.all().count(),
        'total_post':Post.objects.all().count(),
        'total_leader':Leader.objects.all().count(),
        'total_student':Student.objects.all().count(),
        'total_alumni':Alumni.objects.all().count(),
        'total_forum':Forum.objects.all().count(),
       }
    return render(request,'Zusa_admin/admin_dashboard.html',context=dict)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_user_view(request):
	#search engine
	if request.method == 'GET':
		query=request.GET.get('query')
		if query:
			users=User.objects.filter(
				Q(username__icontains=query)|
				Q(first_name__icontains=query)|
				Q(last_name__icontains=query)
			)
		else:
			users=User.objects.all()
	paginator=Paginator(users,per_page=100)
	page_number=request.GET.get('page',1)
	users_obj=paginator.get_page(page_number)
	return render(request,'Zusa_admin/admin_view_user.html',{'users':users})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])	
def admin_view_new_view(request):
	news=Announcement.objects.all()
	paginator=Paginator(news,per_page=4)
	page_number=request.GET.get('page',1)
	news_obj=paginator.get_page(page_number)
	context={'news':news,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'Zusa_admin/admin_view_news.html',context)

#TO SHOW THE CLUBS IN THE SCHOOL AND SEARCH FOR THE CLUB
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_clubs_view(request):
	#search engine
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			clubs=Club.objects.filter(
				Q( Name__icontains=query)
			)
		else:
			clubs=Club.objects.all()
	paginator=Paginator(clubs,per_page=5)
	page_number=request.GET.get('page',1)
	clubs_obj=paginator.get_page(page_number)
	context={'clubs':clubs_obj,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'Zusa_admin/admin_view_club.html',context)


#TO SHOW THE BLOGS POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_post_view(request):
	posts=Post.objects.all().order_by('-created_on')		
	cat_menu=Category.objects.all()
	popular_posts=Post.objects.all().order_by('hit_count_generic')[0:3]
	paginator=Paginator(posts,per_page=3)
	page_number=request.GET.get('page',1)
	posts_obj=paginator.get_page(page_number)
	context={'posts':posts_obj,'paginator':paginator,'page_number':int(page_number),'cat_menu':cat_menu,'popular_posts':popular_posts}
	return render(request,'Zusa_admin/admin_postlist.html',context)

#TO Delete The BLOGS POST
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_delete_post(request,pk):
    post=get_object_or_404(Post,id=pk)
    if post.Photo_Video:
    	post.Photo_Video.delete()
    post.delete()
    return HttpResponseRedirect('/List-Posts')


#TO SHOW THE LEADERS IN THE SCHOOL  COUNSIL 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_leader_view(request):
	leader=Leader.objects.all()
	context={'leader':leader}
	return render(request,'Zusa_admin/admin_view_list_leader.html',context)

#TO SHOW STUDENT
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_student_view(request):
	student=Student.objects.all()
	context={'student':student}
	return render(request,'Zusa_admin/admin_student_view.html',context)


# TO LIST THE ALUMNI AND SEARCH
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_alumniview_view(request):
    alumni=Alumni.objects.all()
    context={'alumni':alumni}
    return render(request,'Zusa_admin/admin_alumni_list_view.html',context)


# TO SHOW of RESULT OF E-CAMPUS VOTE
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_forum_view(request):
    caty_list = positions.objects.all()
    cand = candidate.objects.all().order_by('-total_votes',)
    return render(request, "Zusa_admin/admin_view_forum.html", {'caty_list':caty_list,'cand':cand})


# TO UPDATE STUDENT INFORMATION
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_upadateuser_view(request,pk):
	user=get_object_or_404(User,id=pk)
	form=userForm(instance=user)
	if request.method == "POST":
		form=userForm(request.POST,instance=user)
		if form.is_valid():
			form.save()
			return redirect('admin-view-user')
	return render(request, 'Zusa_admin/update_user.html', {'form': form})

# TO UPDATE NEWS AND ANNOUNCENTS INFORMATION
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_upadatenews_view(request,pk_test):
	news=get_object_or_404(Announcement,id=pk_test)
	form=NewsForm(instance=news)
	if request.method == "POST":
		form=NewsForm(request.POST,request.FILES,instance=news)
		if form.is_valid():
			news=form.save(commit=False)
			news.Author=request.user
			news.save()
			return redirect('admin-view-new')
	return render(request, 'Zusa_admin/update_news.html', {'form': form})

# TO ADD NEWS AND ANNOUNCENTS INFORMATION
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_addnews_view(request):
	form=NewsForm()
	if request.method == "POST":
		form=NewsForm(request.POST,request.FILES)
		if form.is_valid():
			news=form.save(commit=False)
			news.Author=request.user
			news.save()
			return redirect('admin-view-new')
	return render(request, 'Zusa_admin/add_news.html', {'form': form})

#TO ADD THE CLUB  INFORMATION ADMIN
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_addclub_view(request):
	form=clubForm()
	if request.method == "POST":
		form=clubForm(request.POST,request.FILES,)
		if form.is_valid():
			form.save()
		return redirect('admin-view-club')
	context = {'form':form}	
	return render(request,'Zusa_admin/admin_add_club.html',context)

#TO EDIT THE CLUB  INFORMATION ADMIN
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_view_editclub_view(request,pk):
	career=get_object_or_404(Club,id=pk)
	form=clubForm(instance=career)
	if request.method == "POST":
		form=clubForm(request.POST,request.FILES,instance=career)
		if form.is_valid():
			form.save()
		return redirect('admin-view-club')
	context = {'form':form}	
	return render(request,'Zusa_admin/admin_update_club.html',context)

#To delete users in the website
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def delete_user_view(request,pk):
    user=get_object_or_404(User,id=pk)
    user.delete()
    #return redirect('/admin-view-user')
    return HttpResponseRedirect('/admin-view-users')

#TO DELETE NEWS 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_delete_news(request,pk):
    news=get_object_or_404(Announcement,id=pk)
    if news.image:
    	news.image.delete()
    if news.files:
    	news.files.delete()
    news.delete()
    return HttpResponseRedirect('/admin-view-news')

#TO DELETE CLUB 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_club_delete(request,pk):
    club=get_object_or_404(Club,id=pk)
    club.delete()
    return HttpResponseRedirect('/admin-view-clubs')


#TO CREATE USERS IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_user_admin(request):
	form=UserForm()
	if request.method == 'POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('admin-view-user')
	return render(request,'Zusa_admin/Add_user.html', {'form': form})

#TO DELETE FORUM 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_delete_forum(request,pk):
    forum=get_object_or_404(Forum,id=pk)
    forum.delete()
    return HttpResponseRedirect('/Alumni-Forum')

#TO CREATE POSTS IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_post_admin(request):
	form=PostForm()
	if request.method == 'POST':
		form=PostForm(request.POST,request.FILES)
		if form.is_valid():
			Post=form.save(commit=False)
			Post.author=request.user
			Post.save()
			return redirect('admin-view-post')
	return render(request,'Zusa_admin/Add_post_admin.html', {'form': form})


#TO EDIT POSTS IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def edit_post_admin(request,pk_test):
	post=get_object_or_404(Post,id=pk_test)
	form=PostForm(instance=post)
	if request.method == 'POST':
		form=PostForm(request.POST,request.FILES,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect('admin-view-post')
	return render(request,'Zusa_admin/Add_post_admin.html', {'form': form})



#TO CREATE STUDENT LEADER IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_leader_admin(request):
	form=leaderForm()
	if request.method == 'POST':
		form=leaderForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('admin-view-leader')
	return render(request,'Zusa_admin/create_leader_admin.html', {'form': form})

#TO DELETE STUDENT LEADERS 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_student_delete(request,pk):
    leader=get_object_or_404(Leader,id=pk)
    if leader.image:
    	leader.image.delete()
    leader.delete()
    return HttpResponseRedirect('/Student-Leader')

#TO EDIT  STUDENT LEADER IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update_leader_admin(request,pk):
	leader=get_object_or_404(Leader,id=pk)
	form=leaderForm(instance=leader)
	if request.method == 'POST':
		form=leaderForm(request.POST,request.FILES,instance=leader)
		if form.is_valid():
			form.save()
			return redirect('admin-view-leader')
	return render(request,'Zusa_admin/update_leader_admin.html', {'form': form})


#TO CREATE FORUM FOR ALUMNI IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_forum_admin(request):
	form=forumForm()
	if request.method == 'POST':
		form=forumForm(request.POST,request.FILES)
		if form.is_valid():
			Forum=form.save(commit=False)
			Forum.author=request.user
			Forum.save()
			return redirect('admin-view-forum')
	return render(request,'Zusa_admin/create_forum_admin.html', {'form': form})

#TO EDIT FORUM IN ADMIN AREA
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update_forum_admin(request,pk):
	forum=get_object_or_404(Forum,id=pk)
	form=forumForm(instance=forum)
	if request.method == 'POST':
		form=forumForm(request.POST,request.FILES,instance=forum)
		if form.is_valid():
			form.save()
			return redirect('admin-view-forum')
	return render(request,'Zusa_admin/update_forum_admin.html', {'form': form})



#TO SHOW THE LEADERS CATEGORIES IN THE SCHOOL  COUNSIL 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_catergory_view(request):
	return render(request,'Zusa_admin/admin_category.html')

#TO SHOW THE LEADERS CATEGORIES IN THE SCHOOL  COUNSIL 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_category_leader_view(request):
	cats=categerioes.objects.all()
	context={'cats':cats}
	return render(request,'Zusa_admin/admin_category_leader.html',context)
	
#TO ADD CATERGORIES OF LEADERS IN SCHOOL 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def add_leader_catergory(request):
	form=catergoriesForm()
	if request.method == 'POST':
		form=catergoriesForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('categories_leader')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_category.html',context)

	
#TO EDIT CATERGORIES OF LEADERS IN SCHOOL 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def edit_leader_catergory(request,pk):
	cats=get_object_or_404(categerioes,id=pk)
	form=catergoriesForm(instance=cats)
	if request.method == 'POST':
		form=catergoriesForm(request.POST,instance=cats)
		if form.is_valid:
			form.save()
			return redirect('categories_leader')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_category.html',context)

#TO DELETE STUDENT LEADERS 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_catergory_delete(request,pk):
    cats=get_object_or_404(categerioes,id=pk)
    cats.delete()
    return HttpResponseRedirect('/categories_leaders')
    

#TO SHOW THE POSTS CATEGORIES 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_postcats_view(request):
	cat=Category.objects.all()
	context={'cat':cat}
	return render(request,'Zusa_admin/admin_category_post.html',context)
	CategoryForm


#TO ADD CATERGORIES OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def add_post_catergory(request):
	form=CategoryForm()
	if request.method == 'POST':
		form=CategoryForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('categories_post')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_post_category.html',context)

#TO DELETE CATEGORY POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_catergorypost_delete(request,pk):
    cat=get_object_or_404(Category,id=pk)
    cat.delete()
    return HttpResponseRedirect('/categories_post')


#TO EDIT CATERGORIES OF POST  
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def postcatergory_edit(request,pk):
	cat=get_object_or_404(Category,id=pk)
	form=CategoryForm(instance=cat)
	if request.method == 'POST':
		form=CategoryForm(request.POST,instance=cat)
		if form.is_valid:
			form.save()
			return redirect('categories_post')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_post_category.html',context)

#TO View ABOUT PAGE FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_about_view(request):
	about=About.objects.all()
	context={'about':about}
	return render(request,'Zusa_admin/admin_about_page.html',context)	


#TO ADD ABOUT PAGE FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_about_add(request):
	form=aboutForm()
	if request.method == 'POST':
		form=aboutForm(request.POST,request.FILES)
		if form.is_valid:
			form.save()
			return redirect('admin_aboutpage_view')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_aboutpage.html',context)	

#TO EDIT ABOUT PAGE FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_about_edit(request,pk):
	about=get_object_or_404(About,id=pk)
	form=aboutForm(instance=about)
	if request.method == 'POST':
		form=aboutForm(request.POST,request.FILES,instance=about)
		if form.is_valid:
			form.save()
			return redirect('admin_aboutpage_view')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_aboutpage.html',context)	


#TO DELETE STUDENT ABOUT-PAGE
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_aboutpage_delete(request,pk):
    about=get_object_or_404(About,id=pk)
    if about.file:
    	about.file.delete()
    about.delete()
    return HttpResponseRedirect('/About-page')


#TO SHOW HOMEPAGE  
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_home_view(request):
	return render(request,'Zusa_admin/admin_homepage.html')



#TO ADD HOME-PAGE FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_add_Zetech_team(request):
	form=ZetechForm()
	if request.method == 'POST':
		form=ZetechForm(request.POST,request.FILES)
		if form.is_valid:
			form.save()
			return redirect('admin_Zetech')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_page.html',context)	



#TO ADD HOME-PAGE FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_homezetech_view(request):
	team=Zetechteam.objects.all()
	context={'team':team}
	return render(request,'Zusa_admin/admin_teamview.html',context)	


#TO EDIT HOME-PAGE FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_edit_Zetech_team(request,pk):
	team=get_object_or_404(Zetechteam,id=pk)
	form=ZetechForm(instance=team)
	if request.method == 'POST':
		form=ZetechForm(request.POST,request.FILES,instance=team)
		if form.is_valid:
			form.save()
			return redirect('admin_Zetech')
	context={'form':form}
	return render(request,'Zusa_admin/admin_add_page.html',context)	


#TO DELETE ZETECH TEAM 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def view_delete_zetechteam(request,pk):
    team=get_object_or_404(Zetechteam,id=pk)
    if team.Photo:
    	team.Photo.delete()
    elif team.Video:
    	team.Video.delete()
    team.delete()
    return HttpResponseRedirect('/Zetechteam')


#TO ADD HOME-PAGE PICTURE VIEW 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_carsouel_view(request):
	page=Page.objects.all()
	context={'page':page}
	return render(request,'Zusa_admin/admin_carsuoel.html',context)	


#TO  CREATE THE HOMEPAGE CARSUOEL PICTURES
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_page_create(request):
	form=pageForm()
	if request.method == 'POST':
		form=pageForm(request.POST,request.FILES)
		if form.is_valid():
			Page=form.save(commit=False)
			Page.save()
			return redirect('admin_settings_carsusel')
	context={'form':form}
	return render(request,'Zusa_admin/add_pagecarsuoel.html',context)


#TO DELETE CARSUOESL HOMEPAGE
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_carsuoel_delete(request,pk):
    page=get_object_or_404(Page,id=pk)
    if page.image:
    	page.image.delete()
    page.delete()
    return HttpResponseRedirect('/Setting_carsuosel')



#TO EDIT CARSUOEL FILE OF POST 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_edit_Carsuoel(request,pk):
	page=get_object_or_404(Page,id=pk)
	form=pageForm(instance=page)
	if request.method == 'POST':
		form=pageForm(request.POST,request.FILES,instance=page)
		if form.is_valid:
			form.save()
			return redirect('admin_settings_carsusel')
	context={'form':form}
	return render(request,'Zusa_admin/add_pagecarsuoel.html',context)	


#TO ADD CATERGORIES OF POLLS 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def add_post_position(request):
	form=positionForm()
	if request.method == 'POST':
		form=positionForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('postion_view')
	context={'form':form}
	return render(request,'Zusa_admin/add_postion_poll.html',context)



#TO SHOW THE POSTION CATEGORIES 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_postion(request):
	cat=positions.objects.all()
	context={'cat':cat}
	return render(request,'Zusa_admin/admin_category_postion.html',context)


#TO DELETE POSTION POLL
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_postion_delete(request,pk):
    cat=get_object_or_404(positions,id=pk)
    cat.delete()
    return HttpResponseRedirect('/postion_view')


#TO EDIT POSITION  POLL
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def position_edit(request,pk):
	cat=get_object_or_404(positions,id=pk)
	form=positionForm(instance=cat)
	if request.method == 'POST':
		form=positionForm(request.POST,instance=cat)
		if form.is_valid:
			form.save()
			return redirect('postion_view')
	context={'form':form}
	return render(request,'Zusa_admin/add_postion_poll.html',context)



#TO VIEW CANDIDATE FOR ELECTION 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_candidate_view(request):
	caty_list = positions.objects.all()
	cand=candidate.objects.all()
	context={'cand':cand,'caty_list':caty_list}
	return render(request,'Zusa_admin/candidate_view.html',context)	


#TO ADD CANDIDATE IN  POLLS 
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def add_candidate(request):
	form=candidateForm()
	if request.method == 'POST':
		form=candidateForm(request.POST,request.FILES)
		if form.is_valid:
			form.save()
			return redirect('candidate_view')
	context={'form':form}
	return render(request,'Zusa_admin/add_candidate.html',context)


#TO EDIT CANDIDATE POLL
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def candidate_edit(request,pk):
	cand=get_object_or_404(candidate,id=pk)
	form=candidateForm(instance=cand)
	if request.method == 'POST':
		form=candidateForm(request.POST,request.FILES,instance=cand)
		if form.is_valid:
			form.save()
			return redirect('candidate_view')
	context={'form':form}
	return render(request,'Zusa_admin/add_candidate.html',context)


#TO DELETE CANDIDATE  IN POLL
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_cand_delete(request,pk):
    cand=get_object_or_404(candidate,id=pk)
    if cand.Photo:
    	cand.Photo.delete()
    cand.delete()
    return HttpResponseRedirect('/candidate_view')


#TO DISPLAY YOUTUBE VIDEO 
def youtube_video(request):
	video=Youtube.objects.all()
	context={'video':video}
	return render(request,'Zusa_admin/yotubevideo.html',context)


#TO ADD YOUTUBE VIDEO   
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def add_youtube(request):
	form=youtubeForm()
	if request.method == 'POST':
		form=youtubeForm(request.POST,request.FILES)
		if form.is_valid:
			form.save()
			return redirect('youtube_video')
	context={'form':form}
	return render(request,'Zusa_admin/add_youtube.html',context)


#TO EDIT YOUTUBE VIDEO POLL
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def youtube_edit(request,pk):
	video=get_object_or_404(Youtube,id=pk)
	form=youtubeForm(instance=video)
	if request.method == 'POST':
		form=youtubeForm(request.POST,request.FILES,instance=video)
		if form.is_valid:
			form.save()
			return redirect('youtube_video')
	context={'form':form}
	return render(request,'Zusa_admin/add_youtube.html',context)

#TO DELETE YOUTUBE VIDEO  
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_youtube_delete(request,pk):
    video=get_object_or_404(Youtube,id=pk)
    video.delete()
    return HttpResponseRedirect('/youtube_video')
