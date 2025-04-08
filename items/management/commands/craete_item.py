from django.core.management import BaseCommand

from items.models import Item, Subcategory

class Command(BaseCommand):

    def handle(self, *args, **options):
        sub_category = Subcategory.objects.get(id=2)
        item = Item.objects.create(
            sub_category=sub_category,
            image='/home/agbar/Downloads/iphone-16-pro-max-natural-titanium-2-1000x1000.jpg',
            title='iphone',
            description='iphone 13 pro',
            price=78000,
            production='China',
            model='iphone 13 pro',
            is_available=False,
            color='black',

        )
        item.save()
        items  = Item.objects.filter(is_available=False)
        for item in items:
            item.is_available = True
            item.save(update_fields=['is_available'])