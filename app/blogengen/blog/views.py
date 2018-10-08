# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    n = 'David'
    return render(request, 'blog/index.html', context={'name': n})
    
