from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # Запрос в БД, забираем все объекты модели Book
    serializer_class = BooksSerializer  # Указываем класс зериализации для данной модели
