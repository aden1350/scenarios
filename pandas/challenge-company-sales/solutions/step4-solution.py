import pandas as pd
import matplotlib.pyplot as plt


def visualize_sales_by_location(input_file, output_file):
    """Visualize the total sales by location."""
    sales_data = pd.read_csv(input_file).dropna()
    sales_data['location'] = pd.Categorical(sales_data['location'])
    sales_by_location = sales_data.groupby(
        'location')['price'].sum().reset_index()
    plt.bar(sales_by_location['location'], sales_by_location['price'])
    plt.title('Total Sales by Location')
    plt.xlabel('Location')
    plt.ylabel('Total Sales')
    plt.savefig(output_file)


def visualize_sales_by_product(input_file, output_file):
    """Visualize the total sales by product code."""
    sales_data = pd.read_csv(input_file).dropna()
    sales_data['product_code'] = pd.Categorical(sales_data['product_code'])
    sales_by_product = sales_data.groupby(
        'product_code')['price'].sum().reset_index()
    plt.bar(sales_by_product['product_code'], sales_by_product['price'])
    plt.title('Total Sales by Product Code')
    plt.xlabel('Product Code')
    plt.ylabel('Total Sales')
    plt.savefig(output_file)


def visualize_sales_by_day(input_file, output_file):
    """Visualize the total sales by day."""
    sales_data = pd.read_csv(input_file).dropna()
    sales_data['date'] = pd.to_datetime(sales_data['date'])
    sales_by_day = sales_data.groupby('date')['price'].sum().reset_index()
    plt.plot(sales_by_day['date'], sales_by_day['price'])
    plt.title('Total Sales by Day')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.savefig(output_file)
