import graphene
from .types import CategoryType, TransactionType
from .inputs import CategoryInput
from ..models import Transaction, Category, Transaction_Category
from datetime import date
from graphql_jwt.decorators import login_required

class CreateTransaction(graphene.Mutation):
    class Arguments:
        amount = graphene.Float(required=True)
        description = graphene.String(default_value="")
        type = graphene.String(required=True)
        date = graphene.Date(default_value=date.today())
        categories = graphene.List(CategoryInput)

    transaction = graphene.Field(TransactionType)
    ok = graphene.Boolean()

    @login_required
    def mutate(root, info, amount, description, type, date, categories):
        transaction = Transaction.objects.create(
            amount = amount, 
            description = description,
            type = type, 
            date = date, 
            created_by = info.context.user
        )
        for category in categories:
            Transaction_Category.objects.create(
                transaction_id = transaction.id,
                category_id = category.id
            )
        return CreateTransaction(transaction=transaction, ok=True)

class Mutation(graphene.ObjectType):
    create_transaction = CreateTransaction.Field()