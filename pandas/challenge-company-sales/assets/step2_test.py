import unittest
import pandas as pd
import os
import sys
sys.path.append("/home/labex/project")
from step2 import *


class TestPandasChallengeStep2(unittest.TestCase):

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
        os.remove('sales_data_clean.csv')

    def test_clean_data(self):
        clean_data('sales_data', 'sales_data_clean')
        cleaned_data = pd.read_csv('sales_data_clean.csv')
        self.assertTrue(cleaned_data.equals(self.sales_data.dropna()))


if __name__ == '__main__':
    unittest.main()
