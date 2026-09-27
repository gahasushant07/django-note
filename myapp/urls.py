from . import views
from django.urls import path 

urlpatterns = [
path('', views.homepage,name='homepage'),
path('about',views.aboutpage,name='aboutpage'),
path('project',views.projectpage,name='projectpage'),
path('service',views.service,name='service'),
path('contact',views.contact,name='contactpage'),
path('news',views.news,name='newspage'),
]
