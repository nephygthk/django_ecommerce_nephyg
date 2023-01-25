from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product
from account.models import Customer

class TestCartView(TestCase):
    def setUp(self):
        Customer.objects.create(email='admin')
        Category.objects.create(name="phone", slug="phone")
        Product.objects.create(category_id=1, title="tecno spark6",
                            created_by_id=1, slug="tecno-spark6",
                            price="200.00", image="tecno")
        Product.objects.create(category_id=1, title="iphone11",
                            created_by_id=1, slug="iphone11",
                            price="250.00", image="iphone")
        Product.objects.create(category_id=1, title="infinix smart6",
                            created_by_id=1, slug="infinix-smart6",
                            price="200.00", image="infinix")
        
        # here we are adding to product from the ajax in frontend.
        self.client.post(reverse('cart:add_to_cart'),
                        {'productId':1, 'product_qty':1, 'action':'post'}, xhr=True)
        self.client.post(reverse('cart:add_to_cart'),
                        {'productId':2, 'product_qty':2, 'action':'post'}, xhr=True)

    def test_cart_url(self):
        response = self.client.get(reverse('cart:cart_summary'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart_view(self):
        # checking adding new product to cart
        response = self.client.post(reverse('cart:add_to_cart'),
                    {'productId':3, 'product_qty':1, 'action':'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})

        # here we are checking when we add a product that already exist in the cart, it will increase the qty of that paricular product. p2 had two qty, now adding anoth 1 qty makes it 3, so we chck if it will return qty 3
        response = self.client.post(reverse('cart:add_to_cart'),
                        {'productId':2, 'product_qty':1, 'action':'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    # testing removing from cart, note that the data in add test only works in add test so we are working with the two datas in setup.
    def test_remove_from_cart_views(self):
        response = self.client.post(reverse('cart:remove_from_cart'),
                        {'productId':2, 'action':'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal':'1700.00'})

    def test_update_cart_item_view(self):
        response = self.client.post(reverse('cart:update_cart_item'),
                        {'productId':2, 'productQty':3, 'action':'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4, 'subtotal':'2450.00'})

    