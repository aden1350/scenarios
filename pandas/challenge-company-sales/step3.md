### Step 3: Grouping and Aggregating the data

In this step, you will use Pandas to group the data by different variables and compute some aggregate statistics.

#### Requirements:

Calculate total sales by location, product code, and day using `sales_by_location()`, `sales_by_product()`, and `sales_by_day()`, respectively. Each function takes in two arguments, the input file name and the output file name for the calculated data. The output file will contain the calculated data.

#### Example Output

```
Total sales by location:
location
Boston      8500
Miami      10500
New York    7000
San Fran    4500
Name: price, dtype: int64

Total sales by product code:
product_code
A     7500
B    12000
C    16000
D     6000
E     2000
F     7000
Name: price, dtype: int64

Total sales by day:
date
2022-01-01     450
2022-01-02     750
2022-01-03

```
