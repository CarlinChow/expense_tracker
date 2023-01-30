import graphene

class CategoryInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    is_default = graphene.Boolean()

