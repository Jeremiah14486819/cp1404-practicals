import unittest
from guitar import Guitar

class TestGuitar(unittest.TestCase):
    def test_get_age(self):
        guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
        self.assertEqual(guitar.get_age(), 102)  # Adjust based on the current year

    def test_is_vintage(self):
        old_guitar = Guitar("Vintage Guitar", 1950, 1000)
        new_guitar = Guitar("New Guitar", 2020, 1500)

        self.assertTrue(old_guitar.is_vintage())
        self.assertFalse(new_guitar.is_vintage())

    def test_str(self):
        guitar = Guitar("Fender Stratocaster", 1985, 1200.00)
        self.assertEqual(str(guitar), "Fender Stratocaster (1985) : $1200.00")

if __name__ == "__main__":
    unittest.main()
