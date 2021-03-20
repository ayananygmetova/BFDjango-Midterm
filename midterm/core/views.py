from django.shortcuts import render
from rest_framework import viewsets

from core.models import Book, Journal
from core.serialisers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
