from django.contrib import admin
from blog.models import Blog, Comment_blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']

class Comment_blogAdmin(admin.ModelAdmin):
    list_display = ['name',  'phone', 'comment',]
    list_filter = ['status']
    readonly_fields = ('name', 'phone', 'comment', 'ip',  'blog',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment_blog, Comment_blogAdmin)