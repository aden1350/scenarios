import pandas as pd


def read_data_head(input_file: str, output_file: str):
    """Read in the data from the input file and write the first 5 rows to a CSV file."""
    sales_data = pd.read_csv(input_file + '.csv')
    sales_data.head().to_csv(output_file + '.csv', index=False)

if __name__ == '__main__':
    read_data_head('sales_data', 'sales_data_head')
    head_data = pd.read_csv('sales_data_head.csv')
    print(head_data)