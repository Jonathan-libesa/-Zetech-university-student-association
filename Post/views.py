from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.core.paginator import Paginator
from.models import*
from.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from hitcount.views import HitCountDetailView
from django.core import serializers
from django.views import View
# Create your views here.





#TO SHOW THE BLOGS POST AND SEARCH FOR THE POST
@login_required(login_url='login')
def Blog_user(request):
	#search engine
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			posts=Post.objects.filter(
				Q(Title__icontains=query)|
				Q(content__icontains=query)
			)
		else:
			posts=Post.objects.all().order_by('-created_on')
			
	
	cat_menu=Category.objects.all()
	popular_posts=Post.objects.all().order_by('hit_count_generic')[0:3]
	paginator=Paginator(posts,per_page=3)
	page_number=request.GET.get('page',1)
	posts_obj=paginator.get_page(page_number)
	context={'posts':posts_obj,'paginator':paginator,'page_number':int(page_number),'cat_menu':cat_menu,'popular_posts':popular_posts}
	return render(request,'main/blogpost.html',context)



#TO SHOW THE DETAIL OF A POST AND COUNT THE VIEWS
class PostDetail(HitCountDetailView):
	model=Post
	template_name='main/post_detail.html'
	count_hit=True
	form=CommentForm
	def post(self,request,*args,**kwargs):
		form = CommentForm(request.POST)
		if form.is_valid():
			post=self.get_object()
			form.instance.user = request.user
			form.instance.post=post
			form.save()
		return redirect(reverse("post-details",kwargs={'pk':post.pk}))
	
	def get_context_data(self,**kwargs):
		post_comments_count=Comment.objects.all().filter(post=self.object.id).count()
		popular_posts=Post.objects.all().order_by('hit_count_generic')[0:3]
		cat_menu=Category.objects.all()
		post_comments=Comment.objects.all().filter(post=self.object.id)
		total_data=Comment.objects.filter(post=self.object.id).count()
		context=super().get_context_data(**kwargs)
		context.update({
			'form':self.form,
			'post_comments':post_comments,
			'total_data':total_data,
			'post_comments_count':post_comments_count,
			'cat_menu':cat_menu,
			'popular_posts':popular_posts
			})
		return context
#TO SHOW EACH Catergory  ON THE Post 
@login_required(login_url='login')	
def categoryview(request,cats):
	Category=Post.objects.filter(categories=cats)
	popular_posts=Post.objects.all().order_by('hit_count_generic')[0:3]
	paginator=Paginator(Category,per_page=2)
	page_number=request.GET.get('page',1)
	Category_obj=paginator.get_page(page_number)
	context={'Category':Category_obj,'paginator':paginator,'page_number':int(page_number),'cats':cats,'popular_posts':popular_posts}
	return render(request,'main/catergory_list.html',context)
