from django.contrib import admin

from . models import Note
from . models import Folder


admin.site.register(Note)
admin.site.register(Folder)