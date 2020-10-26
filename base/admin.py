from django.contrib import admin
from .models import Category, Country, Actor, Director, Movie


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country)


class ActorAdmin(admin.ModelAdmin):
    list_display_links = "countries"


admin.site.register(Actor)


class DirectorAdmin(admin.ModelAdmin):
    list_display_links = "countries"


admin.site.register(Director)


class MovieAdmin(admin.ModelAdmin):
    list_display_links = ("countries", "categories", "actors", "directors")


admin.site.register(Movie)
