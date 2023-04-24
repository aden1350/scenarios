### Step 2: Cleaning the data

In this step, you will clean the data by removing any missing values, and converting the data types of some columns.

#### Requirements:

Clean and preprocess the data by dropping any rows with missing values and converting the date column to a datetime type using `clean_data()`. The function takes in two arguments, the input file name and the output file name for the cleaned data. The output file will contain the cleaned data.

#### Example Output

```
First 5 rows of cleaned data:
        date location product_code  quantity  price
0 2022-01-01  New York            A        10    100
1 2022-01-01   Boston            B        20    150
2 2022-01-01    Miami            C         5    200
3 2022-01-02  New York            A        15    100
4 2022-01-02   Boston            B        25    150

Last 5 rows of cleaned data:
          date location product_code  quantity  price
245 2022-09-25   Boston            B        20    150
246 2022-09-25    Miami            C        10    200
247 2022-09-26  New York            A        25    100
248 2022-09-26   Boston            B        30    150
249 2022-09-26    Miami            C        15    200

Shape of cleaned data:
(250, 5)
```
