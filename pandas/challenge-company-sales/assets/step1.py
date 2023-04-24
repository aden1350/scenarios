import pandas as pd


def read_data_head(input_file, output_file):
    """Read in the data from the input file and write the first 5 rows to a CSV file."""


if __name__ == '__main__':
    read_data_head('sales_data', 'sales_data_head')
    head_data = pd.read_csv('sales_data_head.csv')
    print(head_data)
