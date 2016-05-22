from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

# Create your views here.

def home(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/login/success/")
    #else:
        # Show an error page
        #return HttpResponseRedirect("/account/register/success/")
    return render_to_response("home.html",{'form':user},context_instance=RequestContext(request))

'''def home(request):
    render(request,"home.html")
'''
    

