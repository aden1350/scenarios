import pandas as pd


def sales_by_location(input_file: str, output_file: str):
    """Calculate total sales by location."""
    sales_data = pd.read_csv(input_file + '.csv').dropna()
    sales_data['location'] = pd.Categorical(sales_data['location'])
    sales_by_location = sales_data.groupby(
        'location')['price'].sum().reset_index()
    sales_by_location.to_csv(output_file + '.csv', index=False)


def sales_by_product(input_file: str, output_file: str):
    """Calculate total sales by product code."""
    sales_data = pd.read_csv(input_file + '.csv').dropna()
    sales_data['product_code'] = pd.Categorical(sales_data['product_code'])
    sales_by_product = sales_data.groupby(
        'product_code')['price'].sum().reset_index()
    sales_by_product.to_csv(output_file + '.csv', index=False)


def sales_by_day(input_file: str, output_file: str):
    """Calculate total sales by day."""
    sales_data = pd.read_csv(input_file + '.csv').dropna()
    sales_data['date'] = pd.to_datetime(sales_data['date'])
    sales_by_day = sales_data.groupby('date')['price'].sum().reset_index()
    sales_by_day.to_csv(output_file + '.csv', index=False)

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