
from django.shortcuts import render

from .models import projects, gallery,activities
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def home(request):
    context={}
    return render(request,"home.html",context)

def about(request):
    context={}
    return render(request,"about.html",context)

def activitiespage(request):
    upd_activities=activities.objects.all()
    context={
        'activities':upd_activities
    }
    return render(request,"activities.html",context)

def contact(request):
    context={}
    return render(request,"contact.html",context)

def donate(request):
    context={}
    return render(request,"donate.html",context)

def gallerypage(request):
    upd_gallery=gallery.objects.all()
    context={
        'gallery':upd_gallery
    }
    return render(request,"gallery.html",context)

def project(request):
    upd_projects=projects.objects.all()
    context={
        'projects':upd_projects
    }
    return render(request,"projects.html",context)