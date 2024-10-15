from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Articles
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    articles = Articles.objects.order_by('-created_at')
    paginator = Paginator(articles , 2)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request , 'index.html' , {
        'title' : 'Articles Page' ,
        'articles' : articles
    })

def single(request , article_id):
    article = Articles.objects.get(id = article_id)
    article = get_object_or_404(Articles , id = article_id)
    return render(request , 'single.html' , {
        'title' : article.title ,
        'article' : article
    })
