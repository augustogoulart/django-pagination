from django.core.paginator import Page
from django.shortcuts import resolve_url
from pytest_django.asserts import assertContains


def test_book_list_get(book_list):
    assertContains(book_list, "Book List")


def test_book_list_context(book_list):
    assert "page_obj" in book_list.context


def test_book_list_context_instance(book_list):
    assert isinstance(book_list.context["page_obj"], Page)


def test_books_per_page(populate_book_list, book_list):
    _10_BOOKS_PER_PAGE = 10
    page = book_list.context["page_obj"]
    assert page.paginator.per_page == _10_BOOKS_PER_PAGE


def test_get_page_from_query_string(populate_book_list, client):
    resp = client.get(f"{resolve_url('book_list')}?page=2")
    page = resp.context["page_obj"]
    assert page.number == 2
