### Step 2: Load Data from Excel File

The second step is to load data from an Excel file using Pandas. We will use the `pd.read_excel()` method to read the Excel file.

```python
# Load data from Excel file
data = pd.read_excel('sales_data.xlsx')

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
