from django.shortcuts import render
from django.http import HttpResponse
from .models import Speech,Speaker
from django.views import generic
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    return render(request,'speech/welcome.html')

def home(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request,'speech/home.html',context)

def about(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request, 'speech/about.html',context)


def Speakview(request):
    context = {
        'queryset': Speaker.objects.all()
    }
    return render(request, 'speech/speaker.html',context)







