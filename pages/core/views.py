from django.shortcuts import render
from django.core.paginator import Paginator

from pages.core.models import Book


def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 25)
    page_number = request.GET.get('page')
    context = {
        "obj_list": paginator.get_page(page_number)
    }

    return render(request, "core/book_list.html", context)
