from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('' , views.index) ,
    path('',views.index , name= 'articles' ),
    path('send' , views.send , name = 'article.send'),
    path('<int:article_id>/' , views.single , name = 'article')

]
