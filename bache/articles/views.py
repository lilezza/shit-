from django.shortcuts import render ,get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Articles , Category
from .forms import SendArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.views.generic import View ,ListView , DetailView ,FormView , UpdateView ,DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.


class ArticleIndex(ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        return Articles.objects.order_by('created_at')

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Articles page :'
        return context

class UserArticlesIndex(ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs['user_id'])
        return user.articles_set.order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Articles page :'
        return context


class SingleArticleView(DetailView):
    model = Articles
    template_name = 'single.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.get_object()
        return context



class SendArticleView(LoginRequiredMixin , PermissionRequiredMixin , FormView):
    template_name = 'send.html'
    form_class = SendArticleForm
    permission_required = ('articles.add_articles',)
    success_url = reverse_lazy('articles:articles')

    # def get_context_data(self , **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context

    def form_valid(self , form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditArticleView(LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    model = Articles
    template_name = 'edit.html'
    form_class = SendArticleForm
    permission_required = ('articles.change_articles',)
    success_url = reverse_lazy('articles:articles')

    def form_valid(self , form):
        form.save()
        return super().form_valid(form)



class DeleteArticleView(LoginRequiredMixin, PermissionRequiredMixin ,DeleteView):
    model = Articles
    template_name = 'delete.html'
    permission_required = ('articles.delete_articles',)
    success_url = reverse_lazy('articles:articles')
