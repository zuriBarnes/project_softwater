from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SubscribeForm

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






























