from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^feedback0/', views.feedback0, name='feedback0'),
        url(r'^feedback1/', views.feedback1, name='feedback1'),
        url(r'^feedback2/', views.feedback2, name='feedback2'),
        )

