from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.mail import send_mail

from .models import Post
import os


def index(request):
    posts_list = Post.objects.order_by('-post_date')
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)


def post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'posts/post.html', {'post': post})


def contact(request):

    if request.method == 'POST':
        message = request.POST['message']
        send_mail("Contact form",
                  message,
                  "djangotestform@gmail.com",
                  ['natat96192@kespear.com'],
                  fail_silently=False,
                  )
    return render(request, 'posts/contact.html')
