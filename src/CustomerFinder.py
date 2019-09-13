from GreatCircle import great_circle
from Customers import Customers

import logging
import argparse


class IntercomTest:
    """
    We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted.
    We want to invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program
    that will read the full list of customers and output the names and user ids of matching customers (within 100km),
     sorted by User ID (ascending).

    You must use the first formula from this Wikipedia article to calculate distance. Don't forget, you'll need to
    convert degrees to radians.

    The GPS coordinates for our Dublin office are 53.339428, -6.257664.

    You can find the Customer list here.

    We're looking for you to produce working code, with enough room to demonstrate how to structure components in a
    small program. Good submissions are well composed. Calculating distances and reading from a file are separate
    concerns. Classes or functions have clearly defined responsibilities.  Poor submissions will be in the form of one
    big function. It’s impossible to test anything smaller than the entire operation of the program, including reading
    from the input file.


    Here are some guidelines when approaching the submission:

    Submit code as if you intended to ship it to production.

    Use whatever language you feel strongest in. It doesn’t have to be one we use.

    Each submission must meet the following requirements:

    Code must be tested. Test cases cover likely problems.

    Please include the output of your program with your submission in a separate file, e.g., output.txt.

    A file explaining how to install, how to execute the code and how to run tests. We may not be familiar with the
    language/framework you used and this helps us to evaluate it.
    """

    MAX_DISTANCE = 100
    INTERCOM_DUBLIN = {"latitude": 53.339428, "longitude": -6.257664}

    def solve(self, filename):
        """
        :param filename: file with customers data
        :return: return invited Customers object
        """
        all_customers = Customers(filename)
        invited_customers = Customers()
        for customer in all_customers:
            distance = great_circle(customer["longitude"],
                                    customer["latitude"],
                                    self.INTERCOM_DUBLIN["longitude"],
                                    self.INTERCOM_DUBLIN["latitude"])
            if distance <= self.MAX_DISTANCE:
                invited_customers.append(customer)

        invited_customers.sort('user_id')
        return invited_customers


def main():
    """
    the program start here
    :return: None
    """

    # logger
    logging.basicConfig(filename="CustomerFinder.log",
                        filemode="a",
                        level=logging.ERROR,
                        format='%(asctime)s [%(levelname)s] %(message)s')

    # Command line arguments
    parser = argparse.ArgumentParser(description='Command line arguments')
    parser.add_argument('file', help='path customers file')
    args = parser.parse_args()

    # Solve the test for given customers file
    test = IntercomTest()
    result = test.solve(args.file)
    result.dump("invited.txt")


if __name__ == '__main__':
    main()
