from django.contrib import admin
<<<<<<< HEAD

from .models import Post, Comment
=======
from  .models import Post, Comment

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']   
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS  
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
<<<<<<< HEAD


# Register your models here.
#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields=['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets  = admin.ShowFacets.ALWAYS
=======
>>>>>>> 3d1a1926739a3ac0c3b9dbd03f0dcc8933cd52df
