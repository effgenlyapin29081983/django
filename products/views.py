from django.shortcuts import render


def index(request):
    context = {'title': 'myShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'myShop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ]
    }
    return render(request, 'products/products.html', context)
