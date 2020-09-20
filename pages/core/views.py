from django.shortcuts import render

from pages.core.models import Book


def book_list(request):
    page_obj = Book.objects.all().per_page(request, 10)
    return render(request, "core/book_list.html", {"page_obj": page_obj})
