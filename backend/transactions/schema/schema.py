import graphene
from graphql_jwt.decorators import login_required
from .types import TransactionType, CategoryType
from ..models import Transaction, Category, Transaction_Category
from django.db.models import Q

class Query(graphene.ObjectType):
    transactions = graphene.List(TransactionType)
    categories = graphene.List(CategoryType)

    @login_required
    def resolve_transactions(parent, info, **kwargs):
        return Transaction.objects.filter(created_by=info.context.user)
    
    @login_required
    def resolve_categories(parent, info, **kwargs):
        return Category.objects.filter(Q(created_by=info.context.user) | Q(is_default=True))