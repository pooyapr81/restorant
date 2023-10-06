from django.contrib import admin
from .models import Blog, Category, Tag, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'category')
    search_fields = ('title', 'description', 'author', 'category.title')
    list_filter = ('created', 'category')


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    search_fields = ('title', 'published', 'slug')
    list_filter = ('published',)


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'update')
    search_fields = ('title', 'published', 'slug', 'update')
    list_filter = ('published', 'update')


admin.site.register(Tag, TagAdmin)

admin.site.register(Comment)
