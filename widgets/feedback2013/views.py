from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from feedback2013.models import Student, Subject, Feedback, Score
from utils.EBUtils import EBUtils

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
    subject.subject_id_list = ','.join([str(item.id) for item in subject.all()])
    return render(request, 'feedback2013/feedback1.html', {'subject' : subject})

def feedback2(request):
    student = Student(chinese_name=request.session['chinese_name'], 
                      english_name=request.session['english_name'],
                      high_school=request.session['high_school'],
                      email=request.session['email'],
                      school_in_china=request.session['school_in_china'],
                      education_in_china=request.session['education_in_china'],
                      year_study_in_au=EBUtils.parse_int(request.session['year_study_in_au']),
                      final_atar_score=EBUtils.parse_float(request.POST['final_atar_score']),
                      uni_and_major=request.POST['uni_and_major'])
    student.save()

    for item in request.POST['subject_id_list'].split(','):
        subjects = Subject.objects.filter(id=int(item))
        subject = subjects[0] if len(subjects) > 0 else None
        if subject is None:
            raise ValueError('Unexpected subject not found')
        study_score = request.POST['study_score_%s' % item]
        study_score = EBUtils.parse_int(study_score)
        scaled_score = request.POST['scaled_score_%s' % item]
        scaled_score = EBUtils.parse_float(scaled_score)

        score = Score(student=student,
                      subject=subject,
                      study_score=study_score,
                      scaled_score=scaled_score,
                      for_2012_2011 = True if request.POST['for_2012_2011_%s' % item] == 'on' else False,
                      remark=request.POST['remark_%s' % item])
        score.save()

    feedback = Feedback(student=student, 
                        comment=request.POST['comment'], 
                        created_date=datetime.now())
    feedback.save()

    return render(request, 'feedback2013/feedback2.html', {})

