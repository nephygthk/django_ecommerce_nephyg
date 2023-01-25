from django.conf import settings

from decimal import Decimal
from store.models import Product


class Cart:

    def __init__(self, request):

        # this gets us the session
        self.session = request.session
        # get session key from request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # check if the key is in the request.session
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty):

        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty':qty}
        self.save()
    
    def __iter__(self):
        # here we get the product from cart, filter the database with the cart product ids to be able to iterate through the list and return the data
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        # here we copy the cart to have a copy of the basket for iteration
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)] ['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        # we are getting the quantity of the items in our cart to display on cart count
        return sum(item['qty'] for item in self.cart.values())

    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def get_total_price(self):

        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(1500.00)

        total = subtotal + Decimal(shipping)
        return total

    def update(self, product, qty):
        product_id = str(product)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        self.save()

    def remove(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True

