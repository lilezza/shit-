from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # path('' , views.index) ,
    path('',views.ArticleIndex.as_view() , name= 'articles' ),
    path('user/<int:user_id>',views.UserArticlesIndex.as_view() , name= 'user.articles' ),
    path('send' , views.SendArticleView.as_view() , name = 'article.send'),
    path('<int:pk>/edit' , views.EditArticleView.as_view() , name = 'article.edit'),
    path('<int:pk>/delete' , views.DeleteArticleView.as_view() , name = 'article.delete'),
    path('<int:pk>/' , views.SingleArticleView.as_view() , name = 'article'),

]
