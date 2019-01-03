from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Gallery
from apps.tags.models import Tag


class GalleryListView(ListView):
    template_name = 'gallery/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryListView, self).get_context_data(
            *args, **kwargs)
        # context['title'] = 'Rejuva Aesthetica | Gallery'
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Gallery.objects.all()
