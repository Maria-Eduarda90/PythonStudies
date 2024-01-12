import unittest

class Contador():
    pass

class IndexTeste(unittest.TestCase):
    def testFoo(self):
        sub = Contador()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()