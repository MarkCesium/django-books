from rest_framework.serializers import ModelSerializer
from .models import Book


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book  # Указываем модель
        fields = "__all__"  # Указываем поля для сериализации
