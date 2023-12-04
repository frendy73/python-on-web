from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Author

def home(request):
    authors_list = Author.objects.all()
    paginator = Paginator(authors_list, 5)  # Показывать по 5 авторов на странице

    page_number = request.GET.get('page')
    authors = paginator.get_page(page_number)

    return render(request, 'home.html', {'authors': authors})
