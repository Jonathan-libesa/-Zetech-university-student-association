from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import*
from django.core.paginator import Paginator
from Club.models import*
# Create your views here.
   


#TO SHOW THE LEADERS IN THE SCHOOL  COUNSIL 
#@login_required(login_url='login')
def leaderview(request):
	leader=Leader.objects.all()
	cat_menu=Club.objects.all()
	#paginator=Paginator(leader,per_page=3)
	#page_number=request.GET.get('page',1)
	#leader_obj=paginator.get_page(page_number)

	context={'leader':leader,'cat_menu':cat_menu}
	return render(request,'main/list_leader.html',context)
