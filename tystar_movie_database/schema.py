import graphene
from graphene_django import DjangoObjectType

from base.models import Actor, Category, Country, Director, Movie


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class Query(graphene.ObjectType):
    category = graphene.Field(CategoryType, name=graphene.String(required=True))
    all_categories = graphene.List(CategoryType)
    country = graphene.Field(CountryType, name=graphene.String(required=True))
    all_countries = graphene.List(CountryType)
    actor = graphene.Field(ActorType, id=graphene.Int())
    all_actors = graphene.List(ActorType)
    director = graphene.Field(DirectorType, id=graphene.Int())
    all_directors = graphene.List(DirectorType)
    movie = graphene.Field(MovieType, id=graphene.Int())
    all_movies = graphene.List(MovieType)

    def resolve_category(self, info, name):
        if name:
            return Category.objects.get(name=name)

        return None

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_country(self, info, name):
        if name:
            return Country.objects.get(name=name)

        return None

    def resolve_all_countries(self, info, **kwargs):
        return Country.objects.all()

    def resolve_actor(self, info, id):
        if id:
            return Actor.objects.prefetch_related("countries").get(id=id)

        return None

    def resolve_all_actors(self, info, **kwargs):
        return Actor.objects.prefetch_related("countries").all()

    def resolve_director(self, info, id):
        if id:
            return Director.objects.prefetch_related("countries").get(id=id)

        return None

    def resolve_all_directors(self, info, **kwargs):
        return Director.objects.prefetch_related("countries").all()

    def resolve_movie(self, info, id):
        if id:
            return Movie.objects.prefetch_related(
                "actors", "countries", "categories"
            ).get(id=id)

        return None

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.prefetch_related("actors", "countries", "categories").all()


schema = graphene.Schema(query=Query)
