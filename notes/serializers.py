from django.db import models
from rest_framework import serializers

from . models import Note, Folder


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'description')

    def create(self, validated_data):
        note = Note.objects.create(
            title=validated_data.get('title'),
        )

        # TODO: Validate folder against current user
        note.folders.add(self.initial_data.get('folder'))

        return note


class FolderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(read_only=True, many=True)

    class Meta:
        model = Folder        
        fields = ('id', 'title', 'notes')
