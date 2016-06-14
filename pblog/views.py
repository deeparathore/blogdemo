from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from models import Post
from controller import Post_detail
p = Post_detail()
from django.contrib.auth.decorators import login_required


# Create your views here.

def registration(request):
 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pblog/login')
    else:
        form = UserCreationForm()
    return render(request,'pblog/registration.html',{'form':form})



def user_login(request):
    msg = ''
    username = password = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/pblog')
    else:
        msg = "Dose not match user name and password"
    return render(request,'pblog/login.html',{'msg':msg})


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/pblog')


def index(request):
    ######################
    postdata = p.shrot_description_post()
    ######################
    return render(request,'pblog/index.html',{'postdata':postdata})

def add_new_post(request):
    name =  request.user.username
  
    userid = request.user.id
    
    if request.method == 'POST':
        #print request.POST
        title = request.POST['title']
        msg = request.POST['content']
        p = Post(user_id=userid,title=title,message=msg)
        p.save()
        return HttpResponseRedirect('/pblog')
    return render(request, 'pblog/newpost.html')

def post_detail(request,post_id):
    postdata = p.single_post_detail(post_id)
    return render(request,'pblog/post_detail.html',{'postdata':postdata})
