### Step 3: Load Data from JSON File

The third step is to load data from a JSON file using Pandas. We will use the `pd.read_json()` method to read the JSON file.

```python
# Load data from JSON file
data = pd.read_json('sales_data.json')

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
