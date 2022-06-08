from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Blog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Blogs'] = Blog.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class Posts(TemplateView):
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user:
            title = self.request.GET.get("title")
            context['Blogs'] = Blog.objects.filter( user = self.request.user)
        else:

            if title != None:
                context['Blogs'] = Blog.objects.filter(title__icontains = title, user = self.request.user)
            else:
                context['Blogs'] = Blog.objects.all()
        return context
@method_decorator(login_required, name='dispatch')
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

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)