from base.models import Movie, Actor, Director, Category, Country


def run(*args):
    Movie.objects.create(
        title="The Matrix",
        year="1999",
        duration="136",
        csfd_url="https://www.csfd.cz/film/9499-matrix/",
    )

    Movie.objects.create(
        title="Dangerous Liaisons",
        year="1988",
        duration="115",
        csfd_url="https://www.csfd.cz/film/3052-nebezpecne-znamosti/",
    )

    Actor.objects.create(
        first_name="Keanu",
        last_name="Reeves",
        date_of_birth="1964-09-02",
        csfd_url="https://www.csfd.cz/tvurce/46-keanu-reeves/",
    )

    Actor.objects.create(
        first_name="Laurence",
        last_name="Fishburne",
        date_of_birth="1961-07-30",
        csfd_url="https://www.csfd.cz/tvurce/47-laurence-fishburne/",
    )

    Director.objects.create(
        first_name="Lilly",
        last_name="Wachowski",
        date_of_birth="1967-12-29",
        csfd_url="https://www.csfd.cz/tvurce/3112-lilly-wachowski/",
    )

    Director.objects.create(
        first_name="Lana",
        last_name="Wachowski",
        date_of_birth="1965-06-21",
        csfd_url="https://www.csfd.cz/tvurce/3113-lana-wachowski/",
    )

    Category.objects.create(
        name="Comedy",
    )

    Category.objects.create(
        name="Sci-Fi",
    )

    Category.objects.create(
        name="Drama",
    )

    Category.objects.create(
        name="Action",
    )

    Country.objects.create(
        name="USA",
    )

    Country.objects.create(
        name="Libanon",
    )

    Country.objects.create(
        name="United Kingdom",
    )
