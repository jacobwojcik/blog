from django.urls import path
from . import views

app_name = 'blogApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('thanks', views.thanks, name='thanks'),
]
