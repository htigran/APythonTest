from Customers import Customers
import unittest


class BasicCustomerTestCase(unittest.TestCase):

    @staticmethod
    def generate_customers_db():
        customers_db = Customers("test_customers.txt")
        customers_db.append({"latitude": "51.8856167", "user_id": 4, "name": "Ian Append", "longitude": "-10.4240951"})
        return customers_db

    def test_normalize(self):
        customers = Customers()
        customer_dict = {"latitude": 53.339428, "longitude": -6.257664}
        customers.normalize(customer_dict)
        self.assertEqual(float, type(customer_dict["latitude"]))
        self.assertEqual(float, type(customer_dict["longitude"]))

    def test_iteration(self):
        all_customers = self.generate_customers_db()
        for customer, id in zip(all_customers, [3, 1, 2, 4]):
            self.assertEqual(id, customer["user_id"])

    def test_sort(self):
        all_customers = self.generate_customers_db()
        all_customers.sort("user_id")
        for customer, id in zip(all_customers, [1, 2, 3, 4]):
            self.assertEqual(id, customer["user_id"])

if __name__ == '__main__':
    unittest.main()
