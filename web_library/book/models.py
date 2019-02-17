from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    rental_status = models.IntegerField("Rental Status")
    summary = models.CharField(max_length=200)
    release_date = models.DateField("Release Date")
    category = models.CharField(max_length=20)
    
    # For datatable usage
    # class Meta:
    #     verbose_name = 'Title'
    #     verbose_name_plural = 'Titles'
    #     ordering = ['title']

    # def __str__(self):
    #     return self.title

# class BookLoan(models.Model):
#     book_id = 
#     borrower = models.CharField(max_length=20)
    


#     You can use the table structure eg. (You can change the following:)
# 1). BookLoan table eg.
# id, book_id, borrower, rent_date, due_date, return_date
# 2). store the latest_book_loan and status of book in Book table
#  latest_book_loan in Book is the foreign key of the latest book loan of book
# eg.     latest_book_loan = models.ForeignKey(BookLoan, on_delete=models.CASCADE, null=True)