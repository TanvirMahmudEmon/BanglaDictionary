from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$','Dictionary.views.dictionarys'),
    url(r'^get/(?P<dictionary_id>\d+)/$','Dictionary.views.dictionary'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'Dictionary.views.language'),  # For Video: 8
    url(r'^like/(?P<dictionary_id>\d+)/$', 'Dictionary.views.like_word'),  # For Video: 13, article = word
    url(r'^search/$', 'Dictionary.views.search_words'),  # For Video No: 16
)