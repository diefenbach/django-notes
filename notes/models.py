from django.db import models


class Note(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title
        

class Folder(models.Model):
    title = models.CharField('Title', max_length=50)
    notes = models.ManyToManyField(Note, related_name='folders', blank=True)

    def __str__(self):
        return self.title
    