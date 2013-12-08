from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return redirect('/feedback2013/feedback0/')

def feedback0(request):
    return render(request, 'feedback2013/feedback0.html', {})

def feedback1(request):
    return render(request, 'feedback2013/feedback1.html', {})

def feedback2(request):
    return render(request, 'feedback2013/feedback2.html', {})

