from django.contrib import admin

from .models import Category, Channel, Server


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    list_filter = ["id", "name"]


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "owner", "category"]
    list_filter = ["id", "name"]


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "owner", "server"]
    list_filter = ["id", "name"]
