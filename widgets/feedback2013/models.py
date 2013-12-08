from django.db import models

class Student(models.Model):
    def __unicode__(self):
        return self.english_name

    chinese_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    high_school = models.CharField(max_length=255)
    email = models.EmailField()
    school_in_china = models.CharField(max_length=255)
    education_in_china = models.CharField(max_length=50)
    year_study_in_au = models.IntegerField()
    final_atar_score = models.FloatField()
    uni_and_major = models.CharField(max_length=255)


class Subject(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=255)
    custom_student_id = models.IntegerField(default=0)


class Score(models.Model):
    def __unicode__(self):
        return '%s: %s' % (self.student, self.subject)
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    study_score = models.FloatField()
    scaled_score = models.FloatField()
    for_2012_2011 = models.BooleanField()
    remark = models.CharField(max_length=255)

class Feedback(models.Model):
    def __unicode__(self):
        return 'Feedback 2013'
    student = models.ForeignKey(Student)
    comment = models.CharField(max_length=560)
    created_date = models.DateTimeField('date created')



