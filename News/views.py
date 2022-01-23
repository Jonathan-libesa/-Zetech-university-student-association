from django.shortcuts import render
from.models import Announcement
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.




#TO SHOW ALL THE NEWS
@login_required(login_url='login')	
def new_view_user(request):
	new=Announcement.objects.all()
	paginator=Paginator(new,per_page=2)
	page_number=request.GET.get('page',1)
	news_obj=paginator.get_page(page_number)
	context={'new':news_obj,'paginator':paginator,'page_number':int(page_number)}
	return render(request,'main/newsview.html',context)