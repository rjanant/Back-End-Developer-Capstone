from django.tests import TestCase
from .restaurent.model import MenuItems

class MenuTest(TestCase):
    
    def instance(self):
        menu_item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(menu_item, "IceCream : 80")


class MenuViewTest(TestCase):
    
    def setup():
        menu_item_one = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        menu_item_two = MenuItem.objects.create(title="Pizza", price=100, inventory=20)
        self.assertEqual(menu_item, "IceCream : 80")


    def test_getall():
        return MenuItem.objects.all()