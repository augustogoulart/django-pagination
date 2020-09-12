from faker import Faker
from pages.core.models import Book


def run():
    fake = Faker()
    Book.objects.bulk_create([Book(
        author=fake.name(),
        title=fake.sentence(),
        published_at=fake.date()
    ) for book in range(1000)])
