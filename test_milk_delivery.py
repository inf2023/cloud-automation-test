"""Unit tests for milk delivery amounts."""

from decimal import Decimal
import unittest

from milk_delivery import calculate_milk_delivery_amount


class MilkDeliveryAmountTests(unittest.TestCase):
    def test_half_liter_at_60_rupees(self):
        amount = calculate_milk_delivery_amount(Decimal("0.5"), Decimal("60"))
        self.assertIsInstance(amount, Decimal)
        self.assertEqual(amount, Decimal("30"))

    def test_one_liter_at_65_rupees(self):
        amount = calculate_milk_delivery_amount(Decimal("1.0"), Decimal("65"))
        self.assertIsInstance(amount, Decimal)
        self.assertEqual(amount, Decimal("65"))

    def test_one_and_half_liters_at_75_rupees(self):
        amount = calculate_milk_delivery_amount(Decimal("1.5"), Decimal("75"))
        self.assertIsInstance(amount, Decimal)
        self.assertEqual(amount, Decimal("112.50"))


if __name__ == "__main__":
    unittest.main()
