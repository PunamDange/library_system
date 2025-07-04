from django.shortcuts import render, redirect
from .models import Book
from .forms import BookModelForm

def list_view(request):
    template_name = "LibraryApp/book_list.html"
    context = {}
    return render(request, template_name, context)

def show_book_view(request):
    qs_of_books = Book.objects.all()
    template_name = "LibraryApp/show_book.html"
    context = {"qs_of_books": qs_of_books}
    return render(request, template_name, context)

def add_book_view(request):
    form = BookModelForm()
    if request.method == "POST":
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/library/show/")
    template_name = "LibraryApp/add_book.html"
    context = {"form":form}
    return render(request, template_name, context)

def update_book_view(request, i):
    lib_obj = Book.objects.get(id=i)
    form = BookModelForm(instance=lib_obj)
    if request.method == "POST":
        form = BookModelForm(request.POST, instance=lib_obj)
        if form.is_valid():
            form.save()
            return redirect("/library/show/")
    template_name = "LibraryApp/update_book.html"
    context = {"form": form}
    return render(request, template_name, context)

def delete_book_view(request,i):
    lib_obj = Book.objects.get(id=i)
    lib_obj.delete()
    return redirect("/library/show/")

def books_by_author_view(request, author_name):
    books = Book.objects.filter(author=author_name)
    template_name = "LibraryApp/books_by_author.html"
    context = {
        "author": author_name,
        "books": books
    }
    return render(request, template_name, context)

