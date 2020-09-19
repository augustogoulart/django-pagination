from django.views.generic import ListView

from pages.core.models import Book


class BookListView(ListView):
    paginate_by = 10
    model = Book


book_list = BookListView.as_view()
