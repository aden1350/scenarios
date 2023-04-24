import unittest
import pandas as pd
import os
import sys
sys.path.append("/home/labex/project")
from step3 import *


class TestPandasChallengeStep3(unittest.TestCase):

    def setUp(self):
        self.sales_data = pd.DataFrame({
            'date': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01'],
            'location': ['New York', 'Chicago', 'Seattle', 'New York', 'New York'],
            'product_code': ['A01', 'B01', 'C01', 'A02', 'B02'],
            'price': [4.99, 12.99, 7.99, 6.99, 9.99],
            'units_sold': [1, 2, 3, 1, 2]
        })
        self.sales_data.to_csv('sales_data.csv', index=False)
        self.expected_sales_by_location = pd.DataFrame({
            'location': ['Chicago', 'New York', 'Seattle'],
            'price': [12.99, 21.97, 7.99]
        })
        self.expected_sales_by_product = pd.DataFrame({
            'product_code': ['A01', 'A02', 'B01', 'B02', 'C01', 'C02'],
            'price': [4.99, 6.99, 12.99, 9.99, 7.99, 11.99]
        })
        self.expected_sales_by_day = pd.DataFrame({
            'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
            'price': [67.86, 54.91, 41.94, 28.97, 28.97]
        })
        self.sales_data.dropna().to_csv('sales_data_clean.csv', index=False)
        self.expected_sales_by_location.to_csv(
            'sales_by_location.csv', index=False)
        self.expected_sales_by_product.to_csv(
            'sales_by_product.csv', index=False)
        self.expected_sales_by_day.to_csv('sales_by_day.csv', index=False)

    def tearDown(self):
        os.remove('sales_data.csv')
        os.remove('sales_data_clean.csv')
        os.remove('sales_by_location.csv')
        os.remove('sales_by_product.csv')
        os.remove('sales_by_day.csv')

    def test_sales_by_location(self):
        sales_by_location('sales_data_clean', 'sales_by_location')
        sales_by_location_data = pd.read_csv('sales_by_location.csv')
        self.assertTrue(sales_by_location_data.equals(
            self.expected_sales_by_location))

    def test_sales_by_product(self):
        sales_by_product('sales_data_clean', 'sales_by_product')
        sales_by_product_data = pd.read_csv('sales_by_product.csv')
        self.assertTrue(sales_by_product_data.equals(
            self.expected_sales_by_product))

    def test_sales_by_day(self):
        sales_by_day('sales_data_clean', 'sales_by_day')
        sales_by_day_data = pd.read_csv('sales_by_day.csv')
        self.assertTrue(sales_by_day_data.equals(self.expected_sales_by_day))


if __name__ == '__main__':
    unittest.main()
