import graphene


# Define GraphQL types for the models
from graphql_system.person.mutations.mutations import Mutation, PersonType
from graphql_system.person.queries.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)