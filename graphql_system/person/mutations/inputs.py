import graphene

class AddressInput(graphene.InputObjectType):
    id = graphene.ID()
    number = graphene.Int(required=True)
    street = graphene.String(required=True)
    city = graphene.String(required=True)
    state = graphene.String(required=True)


class AddressInputForUpdate(graphene.InputObjectType):
    id = graphene.ID()
    number = graphene.Int()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()


class PersonInput(graphene.InputObjectType):
    id = graphene.ID()
    email = graphene.String(required=True)
    name = graphene.String()
    address = AddressInput(required=True)


class PersonInputForUpdate(PersonInput):
    id = graphene.ID()
    email = graphene.String(required=False)
    address = AddressInputForUpdate(required=False)