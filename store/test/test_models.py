from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='phone', slug='phone')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'phone')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name="phone", slug="phone")
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title="tecno spark6",created_by_id=1, slug="tecno-spark6", price="20.00", image="django")
    
    def test_product_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'tecno spark6')


