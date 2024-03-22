from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Purchase(models.Model):
    client = models.ForeignKey(Clients, related_name='purchases',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='purchases')

    def __str__(self):
        return self.client


