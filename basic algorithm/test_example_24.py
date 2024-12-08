#özet: example 24 de ki fonksiyonları ayrı ayrı test et
import unittest
from example_24 import add, subtract

class Test24Function(unittest.TestCase):
    def test_add_function(self):
         result = add(2, 3)
         self.assertEqual(result, 5)

     def test_subtract_function(self):
         result = subtract(8, 2)
         self.assertEqual(result, 6)

 if __name__ == "__main__":
     unittest.main()


#özet: fonksiyonun başına her zaman test koymalısın, birbirine eşit olmayanları kontrol etsin
class TestStringMethods(unittest.TestCase):

    def test_negative_strings(self):
         firstValue = "Zeyra"
         secondValue = "Hindioğlu"

         message = "First value and second value are not equal!"

         self.assertEqual(firstValue, secondValue, message)


 if __name__ == "__main__":
    unittest.main()


#özet: fonksiyonun başına her zaman test koymalısın, birbirine eşit olanları kontrol etsin
class TestStringMethods(unittest.TestCase):

    def test_positive_strings(self):
        firstValue = "Zeyra"
        secondValue = "Zeyra"

        message = "First value and second value are equal!"

        self.assertEqual(firstValue, secondValue, message)


if __name__ == "__main__":
    unittest.main()