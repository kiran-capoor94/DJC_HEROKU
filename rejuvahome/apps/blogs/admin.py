from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title','category','author','featured','status')
    list_filter = ('category', 'author', 'status','featured')
    list_editable = ('status',)

    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)


admin.site.register(Category)