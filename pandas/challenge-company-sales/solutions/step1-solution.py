import pandas as pd


def read_data_head(input_file, output_file):
    """Read in the data from the input file and write the first 5 rows to a CSV file."""
    sales_data = pd.read_csv(input_file + '.csv')
    sales_data.head().to_csv(output_file + '.csv', index=False)
