from Customers import Customers
import unittest


class BasicCustomerTestCase(unittest.TestCase):

    def test_normalize(self):
        customers = Customers()
        customer_dict = {"latitude": 53.339428, "longitude": -6.257664}
        customers.normalize(customer_dict)
        self.assertEqual(float, type(customer_dict["latitude"]))
        self.assertEqual(float, type(customer_dict["longitude"]))

    """
    Similar way we test all other methods
    
    Of course if we do TDD we implement the test first
    """


if __name__ == '__main__':
    unittest.main()
