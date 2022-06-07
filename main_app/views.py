from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Blog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
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
        title = self.request.GET.get("title")
        if title != None:
            context['Blogs'] = Blog.objects.filter(title__icontains = title, user = self.request.user)
        else:
            context['Blogs'] = Blog.objects.filter( user = self.request.user)
        return context

class New(CreateView):
    model = Blog
    fields = ['writer','title', 'img', 'body']
    template_name = "new.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(New, self).form_valid(form)
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})

class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogUpdate(UpdateView):
    model = Blog
    fields =  ['writer','title', 'img', 'body']
    template_name = "blog_update.html"
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})

class BlogDelete(DeleteView):
    model = Blog
    template_name = 'blog_delete_confirmation.html'
    success_url = "/posts/"