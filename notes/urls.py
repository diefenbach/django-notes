from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . views import NotesViewSet, FoldersViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'notes', NotesViewSet)
router.register(r'folders', FoldersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
