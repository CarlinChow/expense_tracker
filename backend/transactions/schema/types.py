import graphene
from ..models import Transaction, Category, Transaction_Category
from graphene_django import DjangoObjectType

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            "id",
            "created_by",
            "name",
            "is_default",
        )

class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "created_by",
            "amount",
            "description",
            "type",
            "date",
        )
    categories = graphene.List(CategoryType)

    def resolve_categories(parent, info, **kwargs):
        # selects tuples with the transaction's id, then projecting only the category attribute
        map_relation = Transaction_Category.objects.filter(transaction_id=parent.id).only('category_id') 
        return Category.objects.filter(id__in=map_relation)