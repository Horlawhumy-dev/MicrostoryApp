from django.contrib import admin

from .models import MicroStory

class MicrostoryAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "title", "is_published")
    list_display_links = ("id", "fullname")
    list_filter = ("title",)

admin.site.register(MicroStory, MicrostoryAdmin)
