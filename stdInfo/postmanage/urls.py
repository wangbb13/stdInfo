#coding: utf-8
from django.conf.urls import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stdInfo.views.home', name='home'),
    url(r'^$', 'postmanage.views.index'),
    url(r'^global_search','postmanage.views.global_search'),
    url(r'^search$', 'postmanage.views.search'),
    url(r'^basic_info$', 'postmanage.views.get_basic_info'),
    url(r'^update_basic_info$', 'postmanage.views.update_basic_info'),
    url(r'^degree_info$', 'postmanage.views.get_degree_info'),
    url(r'^update_degree_info$', 'postmanage.views.update_degree_info'),
    url(r'^award_info$', 'postmanage.views.get_award_info'),
    url(r'^update_award_info$', 'postmanage.views.update_award_info'),
    url(r'^work_info$', 'postmanage.views.get_work_info'),
    url(r'^update_work_info$', 'postmanage.views.update_work_info'),
    url(r'^graduation_info$', 'postmanage.views.get_graduation_info'),
    url(r'^update_graduation_info$', 'postmanage.views.update_graduation_info'),
    url(r'^detail', 'postmanage.views.get_detail'),
    url(r'^import_excel', 'postmanage.views.import_excel'),
    url(r'^export_excel', 'postmanage.views.export_excel'),
)