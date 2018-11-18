from django.urls import path, include

from .views import GalleryListView

app_name = 'gallery'

urlpatterns = [
    path('', GalleryListView.as_view(), name='list'),
]
