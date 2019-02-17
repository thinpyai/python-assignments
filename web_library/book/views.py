from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Book
from .form import BookForm
from django.shortcuts import redirect
from django.utils import timezone
from django.core import serializers
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    if request.user.is_authenticated:
        return render(request, 'book/home.html')
    else:
        return redirect('/login/')

@login_required
def book(request):
    # return render(request, 'book/bookList.html')
    
    # json = serializers.serialize('json', book_list)
    # return HttpResponse(template.render(json, request))

    # return HttpResponse(json, content_type='application/json')
    book_list = Book.objects.all() 
    template = loader.get_template('book/bookList.html')
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))

# to call when datatable is used.
class BookListViewSet(viewsets.ModelViewSet):
    book_list = Book.objects.all() 
    serializer_class = BookSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

@login_required
def add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            #to modify in later
            book.release_date = timezone.now()
            book.rental_status = 0 # 0 is available to rent, 1 is already rent and unavailable to rent again
            book.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'book/addBook.html', {'form': form})

@login_required
def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            #to modify in later
            # book.release_date = timezone.now()
            # book.rental_status = 0 # 0 is available to rent, 1 is already rent and unavailable to rent again
            book.save()
            return redirect('book')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/editBook.html', {'form': form})
    # response = "You're looking at the results of book %s."
    # return HttpResponse(response % book_id)

@login_required
def delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        status = book.delete()
    else:
        form = BookForm(instance=book)
    return redirect('book')

@login_required
def borrow(request, book_id):
    response = "You're looking at the results of book %s to borrow."
    return HttpResponse(response % book_id)