from django.db import models

class BookLoan(models.Model):
    book_id = models.IntegerField()
    borrower = models.CharField(max_length=20)
    rent_date = models.DateField("Rent Date")
    due_date = models.DateField("Due Date")
    return_date = models.DateField("Return Date")

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    # 1 id available, 0 is on-loan
    rental_status = models.IntegerField("Rental Status",default=1)
    summary = models.CharField(max_length=200)
    release_date = models.DateField("Release Date")
    category = models.CharField(max_length=20)
    latest_book_loan = models.ForeignKey(BookLoan, on_delete=models.CASCADE, null=True)
    
    # For datatable usage
    # class Meta:
    #     verbose_name = 'Title'
    #     verbose_name_plural = 'Titles'
    #     ordering = ['title']

    # def __str__(self):
    #     return self.title