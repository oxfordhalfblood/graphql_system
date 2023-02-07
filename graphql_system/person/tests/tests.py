from graphql_system.person.mutations.mutations import Mutation
from graphql_system.person.queries.queries import Query
from django.test.testcases import TestCase
import graphene

from graphql_system.person.tests.factories import PersonFactory, AddressFactory


class TestQueries(TestCase):
    maxDiff = None

    def setUp(self):
        super().setUp()
        first_address = AddressFactory(number=40, street="This Street Suburb", city="Some", state="ACT")
        second_address = AddressFactory(number=4, street="This Street Suburb", city="Some", state="NSW")
        first_person = PersonFactory.create(email="djangotest@hh.com", name="First Last", address=first_address)
        second_person = PersonFactory.create(email="dd@hh.com", name="Second Last", address=second_address)


    def test_list_of_all_person(self):
        query = """
                    query {
                      person {
                        email
                        name
                        address {
                          number
                          street
                          city
                          state
                        }
                      }
                    }
                """
        expected_response = [
            {'email': 'djangotest@hh.com', 'name': 'First Last', 'address': {'number': 40, 'street': 'This Street Suburb', 'city': 'Some', 'state': 'ACT'}},
            {'email': 'dd@hh.com', 'name': 'Second Last', 'address': {'number': 4, 'street': 'This Street Suburb', 'city': 'Some', 'state': 'NSW'}},
        ]

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)

        self.assertIsNone(result.errors)
        self.assertDictEqual({'person': expected_response}, result.data)

    def test_create_person_mutation(self):
        query = """
                    mutation {
                      createPerson(
                        input:{
                            email: "someemail@some.com"
                            name: "some name"
                            address: {
                              number: 99
                              street: "Some Street Suburb"
                              city: "City"
                              state: "ACT"
                            }
                          } 
                    )
                      {
                          person {
                            email
                            name
                            address {
                              number
                              street
                              city
                              state
                            }
                          }
                        }
                    }           
                """

        expected = {'createPerson': {'person': {'email': 'someemail@some.com', 'name': 'some name', 'address': {'number': 99, 'street': 'Some Street Suburb', 'city': 'City', 'state': 'ACT'}}}}

        schema = graphene.Schema(query=Query, mutation=Mutation)
        result = schema.execute(query)

        self.assertIsNone(result.errors)
        self.assertDictEqual(expected, result.data)
