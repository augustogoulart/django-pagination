from django.shortcuts import resolve_url as r
import pytest

from model_bakery import baker

from pages.core.models import Book


@pytest.fixture
def book_list(db, client):
    return client.get(r("book_list"))


@pytest.fixture
def populate_book_list(db, client):
    return baker.make(Book, _quantity=25)
