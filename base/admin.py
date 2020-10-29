from django.contrib import admin

from .models import Actor, Category, Country, Director, Movie


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)


class CountryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


admin.site.register(Country, CountryAdmin)


class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_of_birth",
        "date_of_death",
        "csfd_url",
        "imdb_url",
        "get_movies",
    )
    list_filter = ("countries",)
    search_fields = (
        "countries__name",
        "name",
    )

    def get_movies(self, obj):
        return "\n".join([movie.title for movie in obj.movie_set.all()])


admin.site.register(Actor, ActorAdmin)


class DirectorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_of_birth",
        "date_of_death",
        "csfd_url",
        "imdb_url",
        "get_movies",
    )
    list_filter = ("countries",)
    search_fields = (
        "countries__name",
        "name",
    )

    def get_movies(self, obj):
        return "\n".join([movie.title for movie in obj.movie_set.all()])


admin.site.register(Director, DirectorAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "duration", "get_actors")
    list_filter = (
        "year",
        ("countries", admin.RelatedOnlyFieldListFilter),
        ("categories", admin.RelatedOnlyFieldListFilter),
    )
    search_fields = (
        "title",
        "countries__name",
        "categories__name",
        "actors__name",
    )

    def get_actors(self, obj):
        return "\n".join([actor.name for actor in obj.actors.all()])


admin.site.register(Movie, MovieAdmin)
