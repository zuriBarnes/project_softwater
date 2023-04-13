from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *

def get_thankyou(request):
    msg = 'Thanks for your submission. We will be in touch shortly!'
    return render(request, 'website/thanks.html', {'msg': msg})

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


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            new_sub = form.save()   
            return HttpResponseRedirect('/thanks/')
    else:
        form = SubscribeForm()
        return render(request, 'website/subscribe.html', {'form': form})




















