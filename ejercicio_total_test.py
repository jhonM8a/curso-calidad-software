from ejercicios import total
import unittest

class TestCalcularTotalTest(unittest.TestCase):
    def test_1(self):
        lst=[1,2,3,4]
        resultado = total(lst)
        self.assertEqual(11, resultado)

if __name__ == '__main__':
    unittest.main()