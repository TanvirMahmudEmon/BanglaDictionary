from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm # For Video No: 11


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request): # For Video No: 10
    if request.method == 'POST': # For Video No: 10
        form = MyRegistrationForm(request.POST) # For Video No: 11
        if form.is_valid(): # For Video No: 10
            form.save() # For Video No: 10
            return HttpResponseRedirect('/accounts/register_success') # For Video No: 10

    args = {} # For Video No: 10
    args.update(csrf(request))  # For Video No: 10

    args['form'] = MyRegistrationForm()  # For Video No: 11
    return render_to_response('register.html', args)  # For Video No: 10


def register_success(request): # For Video No: 10
    return render_to_response('register_success.html')  # For Video No: 10
