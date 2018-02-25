# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Arran Baleva'
	args = {'myName':name, 'numbers':numbers}
	return render(request, 'accounts/home.html', args)