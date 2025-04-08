from items.models import Category, Item, Subcategory
from common.models import Footer, Contacts

class TemplateService:
    def get_category(self):
        return Category.objects.all()

    def get_items(self):
        return Item.objects.all()

    def get_subcategory(self, category_id):
        return Subcategory.objects.filter(category=category_id)

    def get_footer(self):
        return Footer.objects.all()

    def get_contacts(self):
        return Contacts.objects.all()


