
from django.shortcuts import render, get_object_or_404
from items.services import TemplateService

def get_category(request):
    data = TemplateService()
    categories = data.get_category()
    items = data.get_items()

    sub_categories = {}
    for category in categories:
        sub_categories[category.id] = data.get_subcategory(category.id)

    footers = data.get_footer()
    contacts = data.get_contacts()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
        'items': items,
        'footers': footers,
        'contacts': contacts,
    }
    return render(request, 'base.html', context)


def get_category_en(request):
    data = TemplateService()
    categories = data.get_category()
    items = data.get_items()

    sub_categories = {}
    for category in categories:
        sub_categories[category.id] = data.get_subcategory(category.id)

    footers = data.get_footer()
    contacts = data.get_contacts()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
        'items': items,
        'footers': footers,
        'contacts': contacts,
    }
    return render(request, 'base_en.html', context)




# def item_det(request, items_id):
#     data = TemplateService()
#
#     # Получаем конкретный товар
#     items = get_object_or_404(data.get_items, id=items_id)
#
#     # Получаем остальные данные (если нужны для шаблона)
#     categories = data.get_category()
#     contacts = data.get_contacts()
#
#     context = {
#         'items': items,  # Основной товар
#         'categories': categories,
#         'contacts': contacts,
#     }
#     return render(request, 'product_detail.html', context)





