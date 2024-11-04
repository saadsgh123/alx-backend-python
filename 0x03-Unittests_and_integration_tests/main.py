from unittest import TestCase
from unittest.mock import Mock, patch


class PaymentProcessor:
    def charge(self, amount):
        # Imagine this method sends a request to an external API to process payment.
        return "Payment processed"


class Order:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        # This method will be tested with a mock to isolate payment processing.
        return self.payment_processor.charge(amount)


class TestOrder(TestCase):
    def test_checkout(self):
        # Create a mock for the payment processor
        mock_processor = Mock()
        mock_processor.charge.return_value = "Mock payment processed"

        # Pass the mock to Order
        order = Order(mock_processor)

        # Call the method we want to test
        result = order.checkout(100)

        # Check if charge() was called with the expected argument
        mock_processor.charge.assert_called_with(100)
        self.assertEqual(result, "Mock payment processed")
