from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


#Combining CBVs and Mixins
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('blog:post_list')
    login_url = reverse_lazy('login')


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'body']
    login_url = reverse_lazy('login')
    def get_success_url(self):
        # Redirect to the detail page of the updated post using self.object.pk
        return reverse('blog:post_detail', args=[self.object.pk])
    

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    login_url = reverse_lazy('login')