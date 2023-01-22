


from decimal import Decimal
from store.models import Product


class Cart:

    def __init__(self, request):

        # this gets us the session
        self.session = request.session
        # get session key from request.session
        cart = self.session.get('cartkey')
        # check if the key is in the request.session
        if 'cartkey' not in request.session:
            cart = self.session['cartkey'] = {}
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

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

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

    def save(self):
        self.session.modified = True
