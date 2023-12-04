from django.shortcuts import render


def index(request):
    context = {
        'store_name': 'ЧАЙХАНА',
        'product_categories': ['Ноутбуки', 'Планшеты', 'Смартфоны', 'Смарт-часы', 'Телевизоры', 'Принтеры', 'МФУ'],
    }
    return render(request, 'index.html', context)
