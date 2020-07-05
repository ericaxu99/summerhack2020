from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Consumer(models.Model):
    first_name = models.CharField(
        max_length=100, help_text='Enter your first name')
    last_name = models.CharField(
        max_length=100, help_text='Enter your last name')
    budget = models.IntegerField(help_text='Enter your max budget')
    items=[]

    #LIST
    # item_name=Item.item_name
    # item_price=Item.price
    # item_quantity=Item.quantity
    # item = models.ManyToManyField(Item, name=item_name, price=item_price, quantity=item_quantity)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('consumer-detail', args=[str(self.id)])


class Store(models.Model):
    name = models.CharField(
        max_length=20, help_text='Enter the name of the store')
    # item_name=Item.item_name
    # item_price=Item.price
    # item_quantity=Item.quantity
    # item = models.ManyToManyField(Item, name=item_name, price=item_price, quantity=item_quantity)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store-detail', args=[str(self.id)])


class Item(models.Model):
    def __init__(self):
        item_name = models.CharField(max_length=100)
        price = models.FloatField()
        category = models.CharField(choices=CATEGORY, max_length=2)
        description = models.TextField()
        quantity = models.IntegerField(default=0)
    CATEGORY = (
        ('F', 'FRUIT'),
        ('V', 'VEGETABLES'),
        ('D', 'DAIRY'),
        ('M', 'MEAT'),
        ('C', 'CARBS'),
        ('JF', 'JUNK FOOD'),
    )
   
    

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("Item-detail", args=[str(self.id)])
