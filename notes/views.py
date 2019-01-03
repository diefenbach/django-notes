from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from . models import Note, Folder
from . serializers import NoteSerializer, FolderSerializer


class NotesViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self): 
        qs = super().get_queryset()
        filter = self.request.query_params.get('q')
        if filter:
            qs = qs.filter(title__contains=filter)
        return qs

class FoldersViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def get_queryset(self): 
        qs = super().get_queryset()
        filter = self.request.query_params.get('q')
        if filter:
            qs = qs.filter(title__contains=filter)
        return qs