import graphene
from graphene_django.types import ObjectType
from graphql_system.person.models import Person, Address
from graphql_system.person.types import PersonType, AddressType


class Query(ObjectType):
    getPerson = graphene.Field(PersonType, id=graphene.Int())
    # address = graphene.Field(AddressType, id=graphene.Int())
    person = graphene.List(PersonType)
    address = graphene.List(AddressType)

    def resolve_getPerson(self, info, **kwargs):
        """
        Retrieves a specific person when ID is given
        """
        id = kwargs.get('id')
        if id is not None:
            return Person.objects.get(pk=id)

        return None

    def resolve_person(self, info, **kwargs):
        """
        Retrieves all person/people
        """
        return Person.objects.all()

    def resolve_address(self,info, **kwargs):
        """
        Retrieves all addresses
        """
        return Address.objects.all()
