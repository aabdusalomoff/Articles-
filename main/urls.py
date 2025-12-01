from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home.as_view(),name = 'home'),
    path('articles/',views.ArticleView.as_view(), name='articles'),
    path('create/',views.ArticleCreate.as_view(),name='create'),
]