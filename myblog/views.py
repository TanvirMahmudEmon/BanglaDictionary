from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Myblog

# Create your views here.


def post_list(request):
    posts = Myblog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Myblog, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})