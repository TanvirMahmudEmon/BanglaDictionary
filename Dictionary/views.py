from django.shortcuts import render
from django.shortcuts import render_to_response
from Dictionary.models import Dictionary
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect # For Video: 12, 14


# Create your views here.


def dictionary(request, dictionary_id =1): # For Video No: 4
    return render_to_response('dictionary.html',
                             {'dictionary': Dictionary.objects.get(id=dictionary_id)})


def dictionarys(request): # For Video No: 4
    language = 'en-us'  # For Video: 8
    session_language = 'en-us'  # For Video: 8

    if 'lang' in request.COOKIES:  # For Video: 8
        language = request.COOKIES['lang']  # For Video: 8

    if 'lang' in request.session:  # For Video: 8
        session_language = request.session['lang']  # For Video: 8

    args = {} # For Video: 16
    args.update(csrf(request)) # For Video: 16

    args['dictionarys'] = Dictionary.objects.all() # For Video: 16
    args['language']  = language # For Video: 16
    args['session_language'] = session_language # For Video: 16

    return render_to_response('dictionarys.html', args)  # For Video: 16


def language(request, language='en_us'): # For Video: 8
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language) # know about this

    request.session['lang'] = language # For Video: 8 # know about this

    return response


def like_word(request, dictionary_id): # For Video: 13
    if dictionary_id: # For Video: 13
        a = Dictionary.objects.get(id=dictionary_id) # For Video: 13
        count = a.likes # For Video: 13
        count += 1 # For Video: 13
        a.likes = count # For Video: 13
        a.save() # For Video: 13

    return HttpResponseRedirect('/dictionarys/get/%s' %dictionary_id)  # For Video: 13


def search_words(request): # For Video No: 16
    if request.method == "POST": # For Video No: 16
        search_text = request.POST['search_text']  # For Video No: 16
    else:
        search_text = ''  # For Video No: 16

    dictionarys = Dictionary.objects.filter(word__contains=search_text)  # For Video No: 16

    return render_to_response('ajax_search.html', {'dictionarys' : dictionarys})  # For Video No: 16