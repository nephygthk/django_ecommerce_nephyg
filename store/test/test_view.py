from importlib import import_module
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings

from account.models import Customer
from store.models import Category, Product
from store.views import all_products


class TestViewFunctions(TestCase):
    def setUp(self):
        self.c = Client()
        # self.factory = RequestFactory()
        Category.objects.create(name="phone", slug="phone")
        Customer.objects.create(email='admin@admin.com')
        self.data1 = Product.objects.create(category_id=1, title="tecno spark6",
                                            created_by_id=1, slug="tecno-spark6",
                                            price="20.00", image="django")

    def test_url_allowed_hosts(self):
        # here we tested our allowed host to make sure domain that are not registered there can not access our website
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

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
        # importing session
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Phonestore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # def test_view_function(self):
    #     # here we are running a test like store page html but we are using another tool called request factory.
    #     request = self.factory.get('/tecno-spark6')
    #     response = all_products(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<title>Phonestore</title>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code, 200)
