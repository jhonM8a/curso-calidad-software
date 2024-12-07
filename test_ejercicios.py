from ejercicios import total,addit, mult, divide, length, reverse, remove_letter, max, odd_numbers, even_numbers, is_even
import unittest

class TestCalcularTotalTest(unittest.TestCase):
    def test_1(self):
        lst=[1,2,3,4]
        resultado = total(lst)
        self.assertEqual(10, resultado)

    def test_2(self):
        x = 1
        result = addit(x)
        self.assertEqual(6, result)

    def test_3(self):
        x = 2
        reultad = mult(x)
        self.assertNotEqual(2, reultad)
        self.assertEqual(14, reultad)

    def test_4(self):
        a=1
        b=1
        result = divide(a,b)
        self.assertEqual(1, result)

    def test_5(self):
        res = length([2])
        self.assertEqual("Less than 5", res)

        res = length("JhonMarioOchoa")
        self.assertEqual("Longer than 5", res)

    def test_6(self):
        result = reverse("ola")
        self.assertNotEqual("ola", result)

    def test_7(self):
        resul = remove_letter("ola", "o")
        self.assertEqual("o", resul)

    def test_8(self):
        result= max([1,10])
        self.assertGreater(result,2)

    def test_9(self):
        res = even_numbers([2,4,3])
        self.assertGreater(len(res), 1)

    def test_10(self):
        resut = odd_numbers([1,2,3,4,5])
        self.assertEqual(len(resut), 3)

    def test_11(self):
        result = is_even(2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()