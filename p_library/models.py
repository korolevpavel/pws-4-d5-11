import datetime
from django.db import models


class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name
    
class Publisher(models.Model):  
    name = models.TextField()  
    
    def __str__(self):
        return self.name

class Friend(models.Model):
    name = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.DO_NOTHING,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name
        
class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.title

class BooksOnHand(models.Model):
    
    friend = models.ForeignKey(Friend, on_delete=models.DO_NOTHING,null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)