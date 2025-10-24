from src.main import add
from unittest import TestCase, main


class TestAdd(TestCase):
    def testAdd(self):
        a = 2
        b = 2
        result = add(a, b)
        self.assertEqual(result, 4, "Summing 2 + 2 does not add up to 4")

if __name__ == "__main__":
    main()
