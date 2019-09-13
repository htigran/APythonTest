import json
import logging


class CustomersIterator:
    """
    Iterator class
    """

    def __init__(self, customers):
        """
        Constructor
        :param customers:
        """
        # Team object reference
        self._customers = customers
        # member variable to keep track of current index
        self._index = 0

    def __next__(self):
        """
        :return: the snext value from team object's lists
        """
        if self._index < (len(self._customers.data)):
            if self._index < len(self._customers.data):
                result = self._customers.data[self._index]
            self._index += 1
            return result
        # End of Iteration
        raise StopIteration


class Customers(object):

        def __init__(self, filename=None):
            """
            Constructor
            :param filename: [optional] file to load customers data
            """
            self.filename = filename
            self.data = []
            if self.filename:
                self.load_customers()

        @staticmethod
        def normalize(customer_dict):
            """
            Normalization of customer data
            :param customer_dict: a customer data
            :return: None
            """
            customer_dict["longitude"] = float(customer_dict["longitude"])
            customer_dict["latitude"] = float(customer_dict["latitude"])

        def try_parse_json(self, line):
            """
            try to construct a json object from given string
            :param line: a string to parse as json
            :return: None
            """
            try:
                json_data = json.loads(line)
                self.normalize(json_data)
                self.data.append(json_data)

            except Exception as e:
                logging.error("Error parsing json string {}\n{}".format(
                    line, e
                ))

        def load_customers(self):
            """
            load customer data from given file
            :return: None
            """
            with open(self.filename) as file:
                for line in file.read().splitlines():
                    self.try_parse_json(line)

        def append(self, customer):
            """
            Add new customer
            :param customer: new customer
            :return: None
            """
            self.data.append(customer)

        def sort(self, key):
            """
            Sort internal customer data based on given key
            :param key: key to sort
            :return: None
            """
            self.data.sort(key=lambda item: item[key])

        def __str__(self):
            """
            :return: string representation of Customers
            """
            result = ""
            for customer in self.data:
                result += str(customer) + "\n"

            return result

        def dump(self, filename):
            """
            Dump Customers into given file
            :param filename: file to dump customers data in
            :return:
            """
            with open(filename, "w") as file:
                file.write(str(self))

        def __iter__(self):
            """
            :return: Customers Iterator
            """
            return CustomersIterator(self)
