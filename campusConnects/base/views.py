from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views import View
from .forms import EventForm,CreateUserform
from .models import Event
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    event = Event.objects.all().values()
    temp = Event.objects.values_list('title')
    for i in temp[1]:
        print(i)
    context = {'event' : event}

    return render(request,'index.html',context)

def UserRegistration(request):
    form = CreateUserform()

    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

    context = {'form':form}
    return render(request,'userRegistration.html',context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)

            return redirect('/profile')
        else:
            messages.success(request,("There was an error logging in.."))
            return redirect('/login')

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)
        if(form.is_valid()):
            event = form.save(commit = False)
            event.user = request.user
            form.save()
            return redirect('/profile')
    else:
        form = EventForm()
    context = {
        'form':form
    }

    return render(request,'registerForm.html',context)

@login_required
def profile(request):
    username = request.user.username
    user_objs = User.objects.get(username = username)
    print(user_objs)
    user = request.user.objects
    print(user)
    past_events = Event.objects.filter(user=user, end_date__lt=timezone.now())
    future_events = Event.objects.filter(user=user, start_date__gte=timezone.now())
    print(past_events)
    context = {'past_events': past_events,
                'user': user,
                'future_events': future_events}

    return render(request, 'profile.html', context)

def event_details(request):
    event = Event.objects.all()
    return render(request,'index.html',{'event' : event})

class DetailView(View):
    def get(self,request,pk,*args, **kwargs):
        detail = Event.objects.get(pk=pk)
        context = {'detail':detail}
        return render(request,'seemore.html',context)

# def incrementViews()

# def seemore(request,id):
#     event = get_object_or_404(Event,pk=id)
#     context = {'event':event}
#     return render(request,'seemore.html',context)
