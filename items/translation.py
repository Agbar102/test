from modeltranslation import translator
from items.models import *


@translator.register(Category)
class CategoryTranslations(translator.TranslationOptions):
    fields = ('name',)

@translator.register(Subcategory)
class SubcategoryTranslations(translator.TranslationOptions):
    fields = ( 'name',)

@translator.register(Item)
class ItemTranslations(translator.TranslationOptions):
    fields = (
        'image',
        'title',
        'description',
        'price',
        'production',
        'model',
        'is_available',
        'color',
    )

