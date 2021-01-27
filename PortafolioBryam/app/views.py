from django.shortcuts import render

def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def portfolio(request):
    return render(request,'app/portfolio.html')

def contact(request):
    return render(request,'app/contact.html')

