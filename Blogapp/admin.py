from django.contrib import admin
from .models import Post, profile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','comment', 'user', 'status')
    list_filter=('status', 'created', 'updated')
    search_fields=( 'user__username', 'comment')
    prepopulated_fields={'slug':('title', )}
    list_editable =('status',)
    date_hierarchy =('created')

admin.site.register(Post, PostAdmin)
admin.site.register( profile)
