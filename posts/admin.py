from django.contrib import admin
from .models import Post, Status

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "body", "author", "created_on"]

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Status)