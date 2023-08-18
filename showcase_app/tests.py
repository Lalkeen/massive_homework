from django.db.models import Q
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from .models import Product
from http import HTTPStatus

# Create your tests here.

Faker.seed("massive_homework")

fake = Faker()


# class TestProductListTestCase(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.product = Product.objects.create(
#             name=fake.user_name(),
#             description=fake.bs(),
#             user_id=1,
#         )

#     @classmethod
#     def tearDownClass(cls):
#         cls.product.delete()

#     def test_get_product(self):
#         qs = Product.objects.filter(~Q(name="default"))
#         count = qs.count()
#         self.assertEqual(count, 1)
#         product = qs.get()
#         self.assertEqual(product.pk, self.product.pk)


class ShowcaseIndexViewTestCase(TestCase):
    def test_index_view_status_ok(self):
        url = reverse("showcase_app:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "showcase_app/product_list.html")
