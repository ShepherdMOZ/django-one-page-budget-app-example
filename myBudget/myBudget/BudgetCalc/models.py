from django.db import models

# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    date = models.DateField()
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9,decimal_places=2)
    note = models.TextField(default=None, blank=True, null= True)
