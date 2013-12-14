from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from feedback2013.models import Subject

def index(request):
    return redirect('/feedback2013/feedback0/')

def feedback0(request):
    return render(request, 'feedback2013/feedback0.html', {})

def feedback1(request):
    request.session['chinese_name'] = request.POST['chinese_name']
    request.session['english_name'] = request.POST['english_name']
    request.session['high_school'] = request.POST['high_school']
    request.session['email'] = request.POST['email']
    request.session['school_in_china'] = request.POST['school_in_china']
    request.session['education_in_china'] = request.POST['education_in_china']
    request.session['year_study_in_au'] = request.POST['year_study_in_au']

    subject = Subject.objects.filter(custom_student_id=0)
    return render(request, 'feedback2013/feedback1.html', {'subject' : subject})

def feedback2(request):
    
    request.session['final_atar_score'] = request.POST['final_atar_score']
    request.session['uni_and_major'] = request.POST['uni_and_major']
    request.session['comment'] = request.POST['comment']

    return render(request, 'feedback2013/feedback2.html', {})

