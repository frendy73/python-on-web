from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DeleteView
from .models import Product
from django.urls import reverse_lazy

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'product_confirm_delete.html'

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')


