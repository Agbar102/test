from modeltranslation import translator
from common.models import Contacts


@translator.register(Contacts)
class ContactsTranslations(translator.TranslationOptions):
    fields = ('company_name',
              'address',
              'phone',
              'working_hours',

               )