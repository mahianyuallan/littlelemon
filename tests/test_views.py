from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Greek Salad", price=12.50, inventory=20)
        Menu.objects.create(title="Bruschetta", price=7.99, inventory=35)
        Menu.objects.create(title="Lemon Dessert", price=5.00, inventory=15)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)
