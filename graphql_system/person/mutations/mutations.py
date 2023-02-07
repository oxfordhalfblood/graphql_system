import graphene

from graphql_system.person.models import Address, Person
from graphql_system.person.mutations.inputs import PersonInput, PersonInputForUpdate
from graphql_system.person.types import PersonType


class CreatePerson(graphene.Mutation):
    # response of mutation
    ok = graphene.Boolean()
    person = graphene.Field(PersonType)

    class Arguments:
        input = PersonInput(required=True)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        address = Address.objects.create(
            number=input.address.number,
            street=input.address.street,
            city=input.address.city,
            state=input.address.state
        )
        person = Person.objects.create(email=input.email, name=input.name, address=address)

        return CreatePerson(ok=ok, person=person)


class UpdatePerson(graphene.Mutation):
    ok = graphene.Boolean()
    person = graphene.Field(PersonType)
    errors = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        input = PersonInputForUpdate(required=True)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        person = Person.objects.filter(pk=id).first()
        if not person:
            return UpdatePerson(ok=ok, person=None)

        ok = True
        if not input.address:
            address = person.address
        if input.address:
            if not all([input.address.number, input.address.street, input.address.city, input.address.state]):
                return UpdatePerson(ok=False, person=None, errors="Fields missing for Address")
            address, created_address = Address.objects.get_or_create(number=input.address.number, street=input.address.street, city=input.address.city, state=input.address.state)

        person.email = input.email
        person.name = input.name
        person.address = address or created_address
        try:
            person.save()
        except Exception as e:
            return UpdatePerson(ok=False, person=person, errors=str(e))
        return UpdatePerson(ok=ok, person=person, errors=None)


class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
