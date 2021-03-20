from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from core.models import Book, Journal
from core.serialisers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if (self.action=='destroy' or self.action=='update' or self.action=='create') and self.request.user.is_super_admin:
            permission_classes= (AllowAny,)
        elif (self.action=='list' or self.action=='retrieve') :
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]



class JournalViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

    def get_permissions(self):
        if (self.action=='destroy' or self.action=='update' or self.action=='create') and self.request.user.is_super_admin:
            permission_classes= (AllowAny,)
        elif (self.action=='list' or self.action=='retrieve') :
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]
