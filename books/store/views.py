from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # Запрос в БД, забираем все объекты модели Book
    serializer_class = BooksSerializer  # Указываем класс сериализация для данной модели

    filter_backends = [DjangoFilterBackend]
    filter_fields = ["price"]
