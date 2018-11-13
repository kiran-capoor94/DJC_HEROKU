# from django.contrib import admin
from django.urls import path, include

from .views import BlogDetailView, BlogListView, BlogFeaturedListView, BlogFeaturedDetailView, BlogArchiveIndexView


app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<slug>/', BlogDetailView.as_view(), name='detail'),
    path('featured/all/', BlogFeaturedListView.as_view(), name='featured_list'),
    path('featured/<slug>/', BlogFeaturedDetailView.as_view(), name='featured_detail'),
    path('archive/all', BlogArchiveIndexView.as_view(), name='archive'),


    # path('categories/all/', CategoryListView.as_view(),name='list_of_category'),
    # path('categories/<slug>/', CategoryListView.as_view(),name='category_detail'),
    # path('archive/<int:year>/', BlogYearArchiveView.as_view(),name="archive_year"),
    # path('archive/<int:year>/<int:month>/', BlogMonthArchiveView.as_view(month_format='%m'),name="archive_month_numeric"),
    # path('archive/<int:year>/<str:month>/', BlogMonthArchiveView.as_view(), name="archive_month"),
]
