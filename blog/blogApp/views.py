from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post
from django.conf import settings
import requests
import os


def index(request):
    posts_list = Post.objects.order_by('-post_date')
    title = "JW Blog"
    context = {'posts_list': posts_list, 'title': title}
    return render(request, 'posts/index.html', context)


def post(request, post_id):
    title = "Post"
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'posts/post.html', {'post': post, 'title': title})


def send_simple_message(mail, message):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox678e6926ab9e49bcaebac55f4bd7a85e.mailgun.org/messages",
        auth=("api", settings.API_KEY),
        data={"from": "Mailgun Sandbox <postmaster@sandbox678e6926ab9e49bcaebac55f4bd7a85e.mailgun.org>",
              "to": "Jakub Wójcik <jacobyv11@gmail.com>",
              "subject": "Your Blog",
              "text": f"Author: {mail}, message: {message}"})


def contact(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        message = request.POST['message']
        send_simple_message(mail, message)
        return HttpResponseRedirect('/thanks')
    title = "Contact"
    return render(request, 'posts/contact.html', {'title': title})


def thanks(request):
    return render(request, 'posts/thanks.html')
