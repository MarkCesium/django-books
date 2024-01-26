from django.test import TestCase
from store.serializers import BooksSerializer
from store.models import Book


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name="Test book 1", price=25)
        book_2 = Book.objects.create(name="Test book 2", price=35)

        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                "id": book_1.id,
                "name": "Test book 1",
                "price": "25.00",  # Указываем таким образом, т.к. price имеет тип Decimals
            },
            {
                "id": book_2.id,
                "name": "Test book 2",
                "price": "35.00",  # Указываем таким образом, т.к. price имеет тип Decimals
            },
        ]

        self.assertEqual(expected_data, data)
