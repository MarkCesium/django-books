from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .models import Book
from .serializers import BooksSerializer
from rest_framework.permissions import IsAuthenticated


class BookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]  # Ограничиваем доступ для не авторизованных

    queryset = Book.objects.all()  # Запрос в БД, забираем все объекты модели Book
    serializer_class = BooksSerializer  # Указываем класс сериализация для данной модели

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ["price"]
    search_fields = ["author_name", "name"]
    ordering_fields = [
        "price",
        "author_name",
    ]  # /book/?ordering=-... - сортировка наоборот


def auth(request):
    return render(request, "oauth.html")
