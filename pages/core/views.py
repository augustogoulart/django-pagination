from django.shortcuts import render
from django.core.paginator import Paginator

from pages.core.models import Book


def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "core/book_list.html", {"page_obj": page_obj})
