# django_blog_2/blogging/admin.py

# got this from the week's class and collaborated with andrew and jon

from django.contrib import admin
from blogging.models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
