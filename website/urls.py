from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('about/',views.about,name='about'),
    path('activities/',views.activitiespage,name='activities'),
    path('contact/',views.contact,name='contact'),
    path('donate/',views.donate,name='donate'),
    path('gallery/',views.gallerypage,name='gallery'),
    path('projects/',views.project,name='projects'),
]