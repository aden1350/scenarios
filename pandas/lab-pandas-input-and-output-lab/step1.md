### Step 1: Load Data from CSV File

The first step is to load data from a CSV file using Pandas. We will use the `pd.read_csv()` method to read the CSV file.

```python
import pandas as pd

# Load data from CSV file
data = pd.read_csv('sales_data.csv')

# Print first 5 rows of the data
print(data.head())
```

Output:

```
      product   region  sales  revenue
0  Product A  Region 1     10      100
1  Product A  Region 2     20      200
2  Product A  Region 3     30      300
3  Product B  Region 1     40      400
4  Product B  Region 2     50      500
```
