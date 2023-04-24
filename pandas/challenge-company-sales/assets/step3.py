import pandas as pd


def sales_by_location(input_file, output_file):
    """Calculate total sales by location."""


def sales_by_product(input_file, output_file):
    """Calculate total sales by product code."""


def sales_by_day(input_file, output_file):
    """Calculate total sales by day."""


if __name__ == '__main__':
    sales_by_location('sales_data_clean', 'sales_by_location')
    sales_by_location_data = pd.read_csv('sales_by_location.csv')
    sales_by_product('sales_data_clean', 'sales_by_product')
    sales_by_product_data = pd.read_csv('sales_by_product.csv')
    sales_by_day('sales_data_clean', 'sales_by_day')
    sales_by_day_data = pd.read_csv('sales_by_day.csv')
    print(sales_by_location_data)
    print(sales_by_product_data)
    print(sales_by_day_data)
