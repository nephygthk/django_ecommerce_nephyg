from django.test import TestCase
from django.utils import timezone
import datetime
from django.utils.timezone import utc

from account.models import Customer
from store.models import Category, Product
from orders.models import Order,OrderItem

class TestOrderModels(TestCase):
    def setUp(self):
        Customer.objects.create(email='admin@admin.com')
        self.category = Category.objects.create(name='phone', slug='phone')
        self.product = Product.objects.create(category_id=1, title="tecno spark6",
                                            created_by_id=1, slug="tecno-spark6",
                                            price="20.00", image="django")

        self.order_data = Order.objects.create(user_id=1, full_name='mike', address1='add1',
                            address2='add2', total_paid=180000.00, order_key='kkttiiooaghs',)

    def test_order_model_entry(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        
        data = self.order_data
        self.assertTrue(isinstance(data, Order))
        self.assertEqual(str(data), str(now))

    def test_order_item_model_entry(self):
        self.data1 = OrderItem.objects.create(order_id=1, product_id=1,price=30000.00,quantity=2)
        data = self.data1
        self.assertTrue(isinstance(data, OrderItem))
        self.assertEqual(str(data), '1')
