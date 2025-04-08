
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from common.models import Footer, Contacts



@admin.register(Footer)
class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Contacts)
class ContactsAdmin(TabbedTranslationAdmin, SingletonModelAdmin):
    pass





