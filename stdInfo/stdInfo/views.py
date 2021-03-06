#coding: utf-8
__author__ = 'Qingfu Wen'
__contact__ = 'thssvince@163.com'
__date__ = '2014-12-04'
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.template.loader import get_template
from django.db import connection
from django.http import HttpResponse
from student.models import Student
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import Http404
import datetime


def index(request):
    if "username" in request.COOKIES:
        name = request.COOKIES["username"]
        user = User.objects.get(username=name)
        if user.is_staff:
            return HttpResponseRedirect('/manage')
        else:
            return HttpResponseRedirect('/student')
    if request.method == 'GET':
        request.session.set_test_cookie()
        return render_to_response("index.html", context_instance=RequestContext(request))
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        clk = request.POST.get('clk', '')
        request.session["username"] = username
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                if clk == "on":
                    dt = datetime.datetime.now() + datetime.timedelta(weeks=3)
                    response = HttpResponseRedirect('/')
                    response.set_cookie("username", username, expires=dt)
                    return response
            else:
                errors = u"请启用cookie再试一次"
                return render_to_response("index.html", {'errors': errors}, context_instance=RequestContext(request))
            if request.user.is_staff:
                return HttpResponseRedirect('/manage')
            else:
                return HttpResponseRedirect('/student')
        else:
            errors = u"用户名或密码错误!"
            return render_to_response("index.html", {'errors': errors}, context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie("username")
    return response


def create_user(request, parm1, parm2):
    try:
        user = User.objects.get(username=parm1)
    except Exception as e:
        user = User(username=parm1)
    user.set_password(parm2)
    user.save()
    return HttpResponse('create user successfully. username:%s, password:%s'%(user.username, user.password))


def del_cookie(request):
    html = "delete cookies"
    response = HttpResponse(html)
    response.delete_cookie("username")
    return response