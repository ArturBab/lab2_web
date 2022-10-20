from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite1.models import Processors, Cards, Plates

def index(request):
    return render(request, 'index.html')



def Getprocessors(request):
    pro = Processors.objects.all()
    return render(request, 'processors.html', { 'pro' : pro })


def GetCards(request):
    card = Cards.objects.all()
    return render(request, 'cards.html', { 'card' : card })

def GetPlates(request):
    pla = Plates.objects.all()
    return render(request, 'plates.html', {'pla' : pla })
# Create your views here.
