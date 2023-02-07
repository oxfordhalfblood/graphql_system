import factory

from graphql_system.person.models import Person, Address

class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

class PersonFactory(factory.django.DjangoModelFactory):
    address = factory.SubFactory(AddressFactory)
    class Meta:
        model = Person