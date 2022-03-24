from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from.models import*
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import F
# Create your views here.

@login_required(login_url='login')
def poll_home(request):
	elec=Electiontype.objects.filter(status=1).all()
	obj=positions.objects.filter(status=1).all()
	context={'obj':obj,'elec':elec}
	return render(request,'polls/polls_home.html',context)


@login_required(login_url='login')
def candidateView(request, pos):
    obj = get_object_or_404(positions, pk = pos)
    if request.method == "POST":

        temp = ControlVote.objects.get_or_create(user=request.user, position=obj)[0]

        if temp.status == False:
            temp2 = candidate.objects.get(pk=request.POST.get(obj.Name))
            temp2.total_votes += 1
            temp2.save()
            temp.status = True
            temp.save()
            messages.success(request,'Successfully voted')
            return HttpResponseRedirect('/voting')
        else:
            messages.warning(request, 'You have already voted for this position.')
            return render(request, 'polls/candidate_h.html', {'obj':obj})
    else:
        return render(request, 'polls/candidate_h.html', {'obj':obj})

@login_required(login_url='login')
def resultView(request):
    caty_list = positions.objects.all()
    cand = candidate.objects.all().order_by('-total_votes',)
    return render(request, "polls/result.html", {'caty_list':caty_list,'cand':cand})


#@login_required(login_url='login')
#def index(request):
    #caty_list = positions.objects.all()
    #context = {'caty_list': caty_list} 
    #return render(request, 'polls/home_voter.html', context)



#@login_required(login_url='login')
#def vote(request):
   #pos=get_list_or_404( positions)
    #for cat in pos:
        #temp = ControlVote.objects.get_or_create(user=request.user, position=pos)[0]
        #selected_choices_pks =request.GET.getlist(cat.Name)
        #selected_choices=candidate.objects.filter(pk__in=selected_choices_pks)
        #selected_choices.update(total_votes=F('total_votes') + 1)
        #selected_choices.update(votes=F('votes')+1)
        #messages.success(request,'Successfully voted')
        #return HttpResponseRedirect('/voting')
    #else:
        #messages.warning(request, 'You have already voted for this position.')
        #return render(request, 'polls/home_voter.html', {'pos':pos})

#def vote(request):
    #pos=get_list_or_404( positions)
    #for cat in pos:
        #temp=ControlVote.objects.get_or_create(user=request.user, position=cat)[0]
        #if temp.status == False:
            #temp2 = cat.candidate_set.get(pk=request.POST[cat.Name])
            #temp2.total_votes += 1
            #temp2.save()
            #temp.status = True
            #temp.save()
            #messages.success(request,'Successfully voted')
            #return HttpResponseRedirect('/voting')
        #else:
            #messages.warning(request, 'You have already voted for this position.')
            #return render(request, 'polls/candidate.html', {'pos':pos})
    #else:
        #return render(request, 'polls/candidate.html', {'pos':pos})