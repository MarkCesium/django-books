from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        # Создаём две записи во ВРЕМЕННУЮ БД
        book_1 = Book.objects.create(name="Test book 1", price=25)
        book_2 = Book.objects.create(name="Test book 2", price=35)

        url: str = reverse("book-list")
        response = self.client.get(url)

        # Сериализуем две созданные сущности
        serialized_data = BooksSerializer([book_1, book_2], many=True).data

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialized_data, response.data)
