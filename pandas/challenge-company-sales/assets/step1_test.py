from step1 import *
import unittest
import pandas as pd
import os
import sys
sys.path.append("/home/labex/project")


class TestPandasChallengeStep1(unittest.TestCase):

    def setUp(self):
        self.sales_data = pd.DataFrame({
            'date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01'],
            'location': ['New York', 'Chicago', 'Seattle', 'New York', 'New York'],
            'product_code': ['A01', 'B01', 'C01', 'A02', 'B02'],
            'price': [4.99, 12.99, 7.99, 6.99, 9.99],
            'units_sold': [1, 2, 3, 1, 2]
        })
        self.sales_data.to_csv('sales_data.csv', index=False)

    def tearDown(self):
        os.remove('sales_data.csv')
        os.remove('sales_data_head.csv')

    def test_read_data_head(self):
        read_data_head('sales_data', 'sales_data_head')
        head_data = pd.read_csv('sales_data_head.csv')
        self.assertTrue(head_data.equals(self.sales_data.head()))


if __name__ == '__main__':
    unittest.main()
