
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from functools import reduce

from django.core.files.storage import FileSystemStorage
from scipy import stats

from .models import CDR, Cases, CDRList, BTSList, BTS
from .forms import CasesForm

import csv
import pandas as pd
import numpy as np

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse


from datetime import datetime


def exam(request):
    context = {'segment': 'exam'}  
    print("exam")  
    html_template = loader.get_template('home/exam.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    print("index")  
    context = {'segment': 'index'}    
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))




@login_required(login_url="/login/")
def home(request):
    print("home")  
    context = {'segment': 'index'}    
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def lms(request):
    print("lms")  
    context = {'segment': 'index'}    
    html_template = loader.get_template('home/lmsdashboard.html')
    return HttpResponse(html_template.render(context, request))






def pages(request):
    print("pages")  
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
