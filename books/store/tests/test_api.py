from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(
            name="Test book 1", price=25, author_name="Author 1"
        )
        self.book_2 = Book.objects.create(
            name="Test book 2", price=35, author_name="Author 2"
        )
        self.book_3 = Book.objects.create(
            name="Test book 3 Author 1", price=35, author_name="Author 3"
        )
        self.book_4 = Book.objects.create(
            name="Test book 4", price=40, author_name="Author 3"
        )

    def test_get(self):
        url: str = reverse("book-list")
        response = self.client.get(url)
        serialized_data = BooksSerializer(
            [
                self.book_1,
                self.book_2,
                self.book_3,
                self.book_4,
            ],
            many=True,
        ).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_search(self):
        url: str = reverse("book-list")
        response = self.client.get(url, data={"search": "Author 1"})
        serialized_data = BooksSerializer([self.book_1, self.book_3], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_filter(self):
        url: str = reverse("book-list")
        response = self.client.get(url, data={"price": 35})
        serialized_data = BooksSerializer([self.book_2, self.book_3], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_ordering_price(self):
        url: str = reverse("book-list")
        response = self.client.get(url, data={"orering": "price"})
        serialized_data = BooksSerializer(
            [
                self.book_1,
                self.book_2,
                self.book_3,
                self.book_4,
            ],
            many=True,
        ).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_ordering_author(self):
        url: str = reverse("book-list")
        response = self.client.get(url, data={"orering": "author_name"})
        serialized_data = BooksSerializer(
            [
                self.book_1,
                self.book_2,
                self.book_3,
                self.book_4,
            ],
            many=True,
        ).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)
