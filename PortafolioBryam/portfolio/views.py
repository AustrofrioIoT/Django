from django.shortcuts import render
from .models import Project,Video

def portfolio(request):
    projects=Project.objects.all()
    obj= Video.objects.all() 
    return render (request,"portfolio/portfolio.html",{'projects':projects,'obj':obj})
