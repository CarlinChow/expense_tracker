from django.db import models
from django.conf import settings

class Transaction(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        if self.type == 'e':
            return "-$" + "{:.2f}".format(self.amount) + "  " + str(self.date)
        else:
            return "$" + "{:.2f}".format(self.amount) + "   " + str(self.date)

class Category(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_default = models.BooleanField()

    def __str__(self):
        return self.name

class Transaction_Category(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction_id.id) + " <-> " + str(self.category_id.id)
 
