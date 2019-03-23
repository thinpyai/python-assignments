from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'book', views.BookListViewSet,base_name='Book')

urlpatterns = [
    path('', views.book, name='book'),
    url('^api/', include(router.urls)),
    path('add/', views.add, name='add'),
    path('<int:book_id>/edit/', views.edit, name='edit'),
    path('<int:book_id>/borrow/', views.borrow, name='borrow'),
    path('<int:book_id>/delete/', views.delete, name='delete'),
    # url(r'^popup/$', views.delete)
]
