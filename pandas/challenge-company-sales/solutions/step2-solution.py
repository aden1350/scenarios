import pandas as pd


def clean_data(input_file, output_file):
    """Clean and preprocess the data by dropping any rows with missing values and
    converting the date column to a datetime type."""
    sales_data = pd.read_csv(input_file + '.csv').dropna()
    sales_data['date'] = pd.to_datetime(sales_data['date'])
    sales_data.to_csv(output_file + '.csv', index=False)
