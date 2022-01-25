from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from.form import StudentSignUpForm,AlumniSignUpForm,UserForm,postForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from validate_email import validate_email
from.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading
from Post.models import *
from Alumni.models import *
from Student.models import*
from django.contrib.auth.models import Group
# Create your views here.


# To MAKE EASIER FOR EMAILING A USER
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

#THE EMAIL BODY TO SEND THE ACTIVATION TO LOGIN
def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('main/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()


#STUDENT REGISTRATION TO LOGIN
@auth_user_should_not_access
def studentpage(request):
    form=StudentSignUpForm()
    if request.method == "POST":
        form=StudentSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='User')
            user.groups.add(group)
            messages.success(request,'Account was created for ' + username)
            user.save()
            send_activation_email(user,request)
            messages.success(request,'We sent you an email to verify your account')
            return redirect('login')
    context={'form':form}
    return render(request,'main/register.html',context)

#ALUMNI REGISTRATION VIEW TO LOGIN
@auth_user_should_not_access
def alumnipage(request):
    form=AlumniSignUpForm()
    if request.method == "POST":
        form=AlumniSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='User')
            user.groups.add(group)
            messages.success(request,'Account was created for ' + username)
            user.save()
            send_activation_email(user,request)
            messages.success(request,'We sent you an email to verify your account')
            return redirect('login')
    context={'form':form}
    return render(request,'main/register.html',context)

#THE ACTIVATE TOKEN FOR THE EMAIL.
def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'main/activate-failed.html', {"user": user})

#THE LOGIN  VIEW FOR ALL USERS
@auth_user_should_not_access
def loginpage(request):
    if request.method == 'POST':
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and not user.is_email_verified:
            messages.add_message(request,messages.WARNING ,'Email is not verified, please check your email inbox')
            return render(request, 'main/login.html', context, status=401)

        if not user:
            messages.add_message(request, messages.WARNING,
                                 'Invalid credentials, try again')
            return render(request, 'main/login.html', context, status=401)

        login(request, user)

        messages.add_message(request, messages.SUCCESS,
                             f'Welcome  {user.username} ')

        return redirect(reverse('admin-dashboard'))

    return render(request, 'main/login.html')


#LOGOUT VIEWS
def logoutUser(request):
    logout(request)
    return redirect('/')

#View Users Profile
@login_required(login_url='login')
def userProfile(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user,}
    return render(request, 'main/Profile.html', context)

#UPDATE USER INFORMATION
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    return render(request, 'main/update-user.html', {'form': form})


#ACCOUNT SETTING
@login_required(login_url='login')
def accountSettings(request):
    user=request.user
    form=UserForm(instance=request.user)
    if request.method == 'POST':
        form=UserForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated Successfully')
    post=Post.objects.filter(author=request.user).order_by('-created_on')
    post_count=Post.objects.filter(author=request.user).count()
    context={'user':user,'post_count':post_count,'form':form,'post':post}
    return render(request, 'main/accountSettings.html', context)


#TO DELETE USER POST
@login_required(login_url='login')
def delete_post_user(request,pk):
    post=get_object_or_404(Post,id=pk)
    if post.Photo:
        post.Photo.delete()
    post.delete()
    return HttpResponseRedirect('/myaccount')


#ADD_POST _USER
@login_required(login_url='login')
def ADD_USER_POST(request):
    form = postForm()
    if request.method == 'POST':
        form=postForm(request.POST,request.FILES)
        if form.is_valid():
            Post=form.save(commit=False)
            Post.author=request.user
            Post.save()
            return redirect('account')
    context={'form':form}
    return render(request,'main/post.html',context)

#User View Profile
@login_required(login_url='login')
def profile_view_user(request):
    user=request.user
    context={'user':user}
    return render(request, 'main/profile_view.html', context)
    