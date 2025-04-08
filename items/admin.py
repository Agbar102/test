from django.contrib import admin
from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin
from .models import Item, Category, Subcategory, Characteristic, User, Cart, CartItem
from modeltranslation.admin import TabbedTranslationAdmin

class CharacteristicInline(TabularInline):
    model = Characteristic


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(SortableAdminMixin,TabbedTranslationAdmin):
    inlines = [CharacteristicInline, ]


@admin.register(Subcategory)
class Subcategory(SortableAdminMixin, TabbedTranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    pass

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, ]

