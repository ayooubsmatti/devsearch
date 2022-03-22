from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('projects/',views.projects,name='projects'),
    path('project-face/<str:pk>',views.project,name='project'),
]
