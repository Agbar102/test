from django.urls import path
from items.views import get_category, get_category_en

front_urlpatterns = [
    path('', get_category, name='ru'),

    path('en', get_category_en, name='en')
]


