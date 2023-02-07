from graphql_system.person.models import Address, Person
from graphene_django.types import DjangoObjectType


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
