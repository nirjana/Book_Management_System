from django.urls import path

from django.contrib import admin
from .import views
urlpatterns=[
    path('new-book/',views.newBook),
    path('add/',views.addBook),
    path('view-books/',views.viewBooks),
    path('delete-book/',views.deleteBook),
    path('edit-book/',views.editBook),
    path('edit/',views.edit),
    path('search-book/',views.searchBook),
    path('search/',views.search),
    path('login/',views.userlogin),
    path('logout/',views.userlogout),
    path('upload/', views.uploader)
]








