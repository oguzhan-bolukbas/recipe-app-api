from django.test import TestCase
from app.calc import add

class CalcTest(TestCase):
    def test_add_numbers(self):
        self.asertEqual(add(3, 8), 11)