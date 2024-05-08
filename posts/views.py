from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView, 
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class PostListView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

class PostDeleteView(DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("list")
