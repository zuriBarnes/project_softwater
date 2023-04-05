from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubscribeForm
from .forms import DemoForm, VolunteerForm

def get_subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        
    else:
        form = SubscribeForm()
    return render(request , 'website/subscribe.html' , {'form': form})


def get_thankyou(request):
    return render(request, 'website/thanks.html')

def get_demo(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = DemoForm()
        return render(request, 'website/demoform.html' , {"form": form})

def get_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = VolunteerForm()
        return render(request, 'website/volunteer.html', {"form": form})























