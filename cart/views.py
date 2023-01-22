from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .cart import Cart
from store.models import Product

def cart_summary(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request, 'cart/cart_summary.html', context)

def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productId"))
        product_qty = int(request.POST.get("product_qty"))
        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, qty=product_qty)

        cartQty = cart.__len__()

        response = JsonResponse({'qty': cartQty })
        return response
    
def remove_from_cart(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productId"))
        cart.remove(product=product_id)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total })
        return response
        
def update_cart_item(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productId"))
        product_qty = int(request.POST.get("productQty"))
        cart.update(product=product_id, qty=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total })
        return response