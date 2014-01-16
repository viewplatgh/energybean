from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.conf.urls import patterns, include, url

from . import views

class EbAdminSite(AdminSite):
	def get_urls(self):
		old_admin_site_urls = super(EbAdminSite, self).get_urls()
		ebadmin_urls = patterns('',
										url(r'^simple_export_fb2013/$', views.simple_export_fb2013, name='simple_export_fb2013')
										)
		return ebadmin_urls + old_admin_site_urls


admin.site = EbAdminSite()