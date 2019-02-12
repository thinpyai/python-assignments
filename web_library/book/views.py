from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Book

def index(request):
    return render(request, 'book/home.html')

def book(request):
    book_list = Book.objects.order_by('-pub_date')
    template = loader.get_template('book/bookList.html')
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    return render(request, 'book/addBook.html')

def edit(request, book_id):
    response = "You're looking at the results of book %s."
    return HttpResponse(response % book_id)

def borrow(request, book_id):
    response = "You're looking at the results of book %s to borrow."
    return HttpResponse(response % book_id)