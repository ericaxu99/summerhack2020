from django.contrib import admin
from .models import Item, Consumer, Store

# Register your models here.
class ItemInLine(admin.TabularInline):
    model = Item

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'budget')
    fields=['first_name', 'last_name', 'budget']
    inlines = [ItemInLine]
    # fieldsets = (
    #     ('User Info', {
    #         'fields': ('first_name', 'last_name')
    #     }),
    #     ('Items List', {
    #         'fields': ()  # list of items in detail view
    #     }),
    # )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    fields=['name']
    inlines = [ItemInLine]
    # fieldsets = (
    #     ('Store Info', {
    #         'fields': ('name')
    #     }),
    #     ('Items List', {
    #         'fields': ()  # list of items in detail view
    #     }),
    # )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category')
    list_filter = ('CATEGORY')
    fields = ['item_name', 'price', 'description', 'category', 'quantity']
    # maybe which store its from and the quantity?
    



