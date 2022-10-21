"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reference_book import views as rb_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_author/<int:pk>/', rb_views.Author.ShowAutor.as_view()),
    path('show_authors/', rb_views.Author.ListAuthor.as_view()),
    path('create_author/', rb_views.Author.CreateAuthor.as_view()),
    path('update_author/<int:pk>/', rb_views.Author.UpdateAuthor.as_view()),
    path('delete_author/<int:pk>/', rb_views.Author.DeleteAuthor.as_view()),
    path('show_serie/<int:pk>/', rb_views.BkSerie.ShowSerie.as_view()),
    path('show_series/', rb_views.BkSerie.ListSerie.as_view()),
    path('create_serie/', rb_views.BkSerie.CreateSerie.as_view()),
    path('update_serie/<int:pk>/', rb_views.BkSerie.UpdateSerie.as_view()),
    path('delete_serie/<int:pk>/', rb_views.BkSerie.DeleteSerie.as_view()),
    path('show_genre/<int:pk>/', rb_views.BkGenre.ShowGenre.as_view()),
    path('show_genres/', rb_views.BkGenre.ListGenre.as_view()),
    path('create_genre/', rb_views.BkGenre.CreateGenre.as_view()),
    path('update_genre/<int:pk>/', rb_views.BkGenre.UpdateGenre.as_view()),
    path('delete_genre/<int:pk>/', rb_views.BkGenre.DeleteGenre.as_view()),
    path('show_publisher/<int:pk>/', rb_views.BkPublisher.ShowPublisher.as_view()),
    path('show_publishers/', rb_views.BkPublisher.ListPublisher.as_view()),
    path('create_publisher/', rb_views.BkPublisher.CreatePublisher.as_view()),
    path('update_publisher/<int:pk>/', rb_views.BkPublisher.UpdatePublisher.as_view()),
    path('delete_publisher/<int:pk>/', rb_views.BkPublisher.DeletePublisher.as_view()),
    path('show_currency/<int:pk>/', rb_views.BkCurrency.ShowCurrency.as_view()),
    path('show_currencys/', rb_views.BkCurrency.ListCurrency.as_view()),
    path('create_currency/', rb_views.BkCurrency.CreateCurrency.as_view()),
    path('update_currency/<int:pk>/', rb_views.BkCurrency.UpdateCurrency.as_view()),
    path('delete_currency/<int:pk>/', rb_views.BkCurrency.DeleteCurrency.as_view()),
]
