# Create a fixture using the graphql_query helper and `client` fixture from `pytest-django`.
import pytest

# from graphene_django.utils.testing import graphql_query
# from graphene.test import Client
# from tystar_movie_database.schema import schema

# @pytest.fixture
# def client_query(client):
#     def func(*args, **kwargs):
#         return graphql_query(*args, **kwargs, client=client)

#     return func

# def test_some_query(client_query):
#     response = client_query(
#         '''
#         query {
#             all_categories {
#                 id
#                 name
#             }
#         }
#         ''',
#         op_name='all_categories'
#     )

#     content = json.loads(response.content)
#     assert 'errors' not in content

# @pytest.fixture
# def graphql_client():
#     return Client(schema)

# from model_bakery import baker

# @pytest.mark.django_db
# class TestMyModelData:
#     @pytest.fixture
#     def query(self):
#         return """
#         query testGetMyModel($searchParam: String!) {
#             myModelData(searchParam: $searchParam) {
#                 totalCount
#             }
#         }
#         """

#     @pytest.fixture
#     def my_model(self):
#         baker.make(
#         "myapp.MyModel",
#         total_count="20", # Decimal field
#         )

#     def test_none_response(self, graphql_client, query, my_model):
#         executed = graphql_client.execute(query, variables={"searchParam": "skittles"})
#         assert executed == {"data": {"myModelData": None}}

# def test_hey():
#     client = Client(schema)
#     executed = client.execute('''
#         query {
#             allCategories {
#                 name
#             }
#         }
#     ''')
#     breakpoint()
#     assert executed == {
#         'data': {
#             'allCategories': 'hello!'
#         }
#     }

# "allCategories", "allActors", "category", "allCountries" or "allMovies"


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
