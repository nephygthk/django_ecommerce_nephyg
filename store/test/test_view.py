from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


class TestViewFunctions(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="phone", slug="phone")
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title="tecno spark6",
                                            created_by_id=1, slug="tecno-spark6",
                                            price="20.00", image="django")

    def test_storepage_url(self):
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        # here we are testing to see if category details url works properly by returning status code 200
        response = self.c.get(reverse('store:category_list', args=["phone"]))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        # here we are testing to see if product details url works properly by returning status code 200
        response = self.c.get(reverse('store:product_detail', args=["tecno-spark6"]))
        self.assertEqual(response.status_code, 200)

    def test_storepage_html(self):
        # here we text our store page html with httprequest. by sending http request to our home page
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Store</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        # here we are running a test like store page html but we are using another tool called request factory.
        request = self.factory.get('/product/tecno-spark6')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Store</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
