from django.shortcuts import render ,get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Articles
from .forms import SendArticleForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    articles = Articles.objects.order_by('created_at')
    paginator = Paginator(articles , 3)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request , 'index.html' , {
        'title' : 'Articles Page' ,
        'articles' : articles ,
        'paginator' : paginator
    })

def single(request , article_id):
    article = Articles.objects.get(id = article_id)
    article = get_object_or_404(Articles , id = article_id)
    return render(request , 'single.html' , {
        'title' : article.title ,
        'article' : article
    })

def send(request):
    if request.method == 'POST':
        # Validation data
        form = SendArticleForm(request.POST)

        if form.is_valid():
            Articles.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                published_at = form.cleaned_data ['published_at']
            )

            return redirect('articles:articles')


    else :
        form = SendArticleForm()

    return render(request , 'send.html' , { 'form' : form })
