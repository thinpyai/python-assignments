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
            # to modify in later
            book.release_date = timezone.now()
            # 0 is available to rent, 1 is already rent and unavailable to rent again
            book.rental_status = 0
            book.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'book/addBook.html', {'form': form})


@login_required
def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if (book.rental_status == 0):
        if request.method == "POST":
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book')
        else:
            form = BookForm(instance=book)
    return render(request, 'book/editBook.html', {'form': form})


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
    book = get_object_or_404(Book, id=book_id)
    if (book.rental_status == 0):
        # Change to show available
        book.rental_status = 1
        status = "Available"
        btn_text = "Return"
    else:
        # Change to show on-loan
        book.rental_status = 0
        status = "On Loan"
        btn_text = "Borrow"

    template = loader.get_template('book/borrowBook.html')
    context = {
        'title': book.title,
        'status' : status,
        'btn_text' : btn_text
    }
    return HttpResponse(template.render(context, request))
    # template_name = 'polls/detail.html'
    # book = get_object_or_404(Book, id=book_id)
    
    # form = BookForm(request.GET, instance=book) 
    # if form.is_valid():
    #     book = form.save(commit=False)
    #     book
    #     # update foreign key
    #     book.save()
    #     return redirect('book')
    # else:
    #     form = BookForm(instance=book)
    # return render(request, 'book/borrowBook.html', {'form': form})
