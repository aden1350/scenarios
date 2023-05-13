# Step 2 Cleaning the data

In this step, you will clean the data by removing any missing values, and converting the data types of some columns.

## Requirements

Clean and preprocess the data by dropping any rows with missing values and converting the date column to a datetime type using `clean_data()`. The function takes in two arguments, the input file name and the output file name for the cleaned data. The output file will contain the cleaned data.

## Example Output

         date  location product_code  quantity  price
0  2022-01-01  New York            A      10.0    100
1  2022-01-01    Boston            B      20.0    150
2  2022-01-01     Miami            C       5.0    200
3  2022-01-02  New York            A      15.0    100
4  2022-01-02    Boston            B      25.0    150
5  2022-01-02     Miami            C      10.0    200
6  2022-01-03  New York            A      20.0    100
7  2022-01-03    Boston            B      30.0    150
8  2022-01-03     Miami            C      15.0    200
