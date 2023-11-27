from django.shortcuts import render
from .models import Book
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def helloview(request):
    books= Book.objects.all()
    return render (request, "viewbook.html", {"books":books})


def addbook(request):
    return render (request, "addbook.html")

def addbookview(request):
        if request.method == "POST":
            title=request.POST["title"]
            price=request.POST["price"]
            book = Book()
            book.title=title
            book.price= price
            book.save()
            return HttpResponseRedirect ("/")
def editbook(request):
     book= Book.objects.get(id=request.GET['bookid'])
     return render(request, "editbook.html", {"book":book})
     
def edit(request):
     if request.method == "POST":
            title=request.POST["title"]
            price=request.POST["price"]
            book = Book.objects.get(id=request.POST['bookid'])
            book.title=title
            book.price= price
            book.save()
            return HttpResponseRedirect ("/")
def deletebook(request):
     book= Book.objects.get(id=request.GET['bookid'])
     book.delete()
     return HttpResponseRedirect ("/")