from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    inventory = models.ManyToManyField('Item')
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    zone = models.CharField(max_length=25)
    #stores = models.ManyToManyField('Store')
    
    def __str__(self):
        return self.name + " ($" + self.price.__str__() + ")"
    
class ShopList(models.Model):
    name = models.CharField(max_length=50)
    contents = models.ManyToManyField('Item', related_name="+", blank=True)
    
    def __str__(self):
        return self.name