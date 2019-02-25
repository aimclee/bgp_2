from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def certificate(request):
    return render(request, 'likelion_6th_certificate.html')