from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Blog
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# class Post:
#     def __init__(self, author, title, body, img):
#         self.author = author
#         self.title = title
#         self.body = body
#         self.img = img

# letters = [
#     Post('Unknown Author', 'The Best Quote', 'Write A Wise Saying And Your Name Will Live Forever!', 'https://thomasguettler.files.wordpress.com/2021/02/wiseman.jpg'),
#     Post('Cat', 'Purr', 'Meow Meow, Meow Meow Mew Meow, MEOW!! HISS! The End!', 'https://ih1.redbubble.net/image.3087347788.1442/st,small,507x507-pad,600x600,f8f8f8.jpg')
# ]


class Posts(TemplateView):
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Blogs'] = Blog.objects.all()
        return context

class New(CreateView):
    model = Blog
    fields = ['writer','title', 'img', 'body']
    template_name = "new.html"
    success_url = '/posts/'

class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'