from django.contrib import admin
from .models import Tool, Library

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')  # Add image here to display in admin

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')  # Add image here to display in admin

admin.site.register(Tool, ToolAdmin)
admin.site.register(Library, LibraryAdmin)
