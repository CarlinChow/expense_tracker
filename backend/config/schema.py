import graphene
import users.schema as usersApp
from transactions.schema import schema as transactionsQuery, mutations as transactionsMutation

class Query( # root query
    usersApp.Query,
    transactionsQuery.Query,
    graphene.ObjectType
):
    pass

class Mutation( # root mutation
    usersApp.Mutation,
    transactionsMutation.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

