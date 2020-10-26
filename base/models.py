from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel, models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Country(TimeStampedModel, models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "countries"


class Actor(TimeStampedModel, models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    csfd_url = models.CharField(unique=True, max_length=250, blank=True, null=True)
    imdb_url = models.CharField(unique=True, max_length=250, blank=True, null=True)

    countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def name(self):
        return f"{self.last_name} {self.first_name}"


class Director(TimeStampedModel, models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    csfd_url = models.CharField(unique=True, max_length=250, blank=True, null=True)
    imdb_url = models.CharField(unique=True, max_length=250, blank=True, null=True)

    countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def name(self):
        return f"{self.last_name} {self.first_name}"


class Movie(TimeStampedModel, models.Model):
    title = models.CharField(max_length=250)
    year = models.SmallIntegerField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    csfd_url = models.CharField(unique=True, max_length=250, blank=True, null=True)
    imdb_url = models.CharField(unique=True, max_length=250, blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return self.title
