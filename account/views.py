from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf 
from .forms import RegForm
#from .forms import LoginForm


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/account/register/success/")
    else:
        form = RegForm()
    return render_to_response("register.html", {'form':form}, context_instance=RequestContext(request))

def reg_success(request):
    context = {'action': '注册'}
    return render_to_response("success.html", context)

def login_success(request):
    context = {'action': '登录'}
    return render_to_response("success.html", context)

'''def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username},context_instance=RequestContext(request))
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
'''

'''def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                return render_to_response('success.html',{'username':username},context_instance=RequestContext(request))
            else:
                return HttpResponseRedirect('/account/login/')
    else:
        form = LoginForm()
    return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
'''
