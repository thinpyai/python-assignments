from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.book, name='book'),
    path('add/', views.add, name='add'),
    path('<int:book_id>/edit/', views.edit, name='edit'),
    path('<int:book_id>/borrow/', views.borrow, name='borrow')
]
