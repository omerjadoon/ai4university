

from django.urls import path, re_path
from apps.home import views
from django.urls import re_path as url

urlpatterns = [


path('', views.index, name='home'),
url('home', views.home, name='dashboard'),
url('exam', views.exam, name='exam'),
url('login', views.home, name='login'),
url('lms', views.lms, name='lms'),
    
    
    # Matches any html file
re_path(r'^.*\.*', views.pages, name='pages'),

]
