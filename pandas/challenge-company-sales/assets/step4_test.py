import unittest
import pandas as pd
import os
import sys
sys.path.append("/home/labex/project")
from step4 import *


class TestPandasChallengeStep4(unittest.TestCase):

    def setUp(self):
        self.sales_data = pd.DataFrame({
            'date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01'],
            'location': ['New York', 'Chicago', 'Seattle', 'New York', 'New York'],
            'product_code': ['A01', 'B01', 'C01', 'A02', 'B02'],
            'price': [4.99, 12.99, 7.99, 6.99, 9.99],
            'units_sold': [1, 2, 3, 1, 2]
        })
        self.sales_data.to_csv('sales_data.csv', index=False)
        self.sales_data.dropna().to_csv('sales_data_clean.csv', index=False)

    def tearDown(self):
        os.remove('sales_data.csv')
        os.remove('sales_data_clean.csv')
        os.remove('sales_by_location.png')
        os.remove('sales_by_product.png')
        os.remove('sales_by_day.png')

    def test_visualize_sales_by_location(self):
        visualize_sales_by_location('sales_data_clean', 'sales_by_location.png')
        self.assertTrue(os.path.exists('sales_by_location.png'))

    def test_visualize_sales_by_product(self):
        visualize_sales_by_product('sales_data_clean', 'sales_by_product.png')
        self.assertTrue(os.path.exists('sales_by_product.png'))

    def test_visualize_sales_by_day(self):
        visualize_sales_by_day('sales_data_clean', 'sales_by_day.png')
        self.assertTrue(os.path.exists('sales_by_day.png'))


if __name__ == '__main__':
    unittest.main()
