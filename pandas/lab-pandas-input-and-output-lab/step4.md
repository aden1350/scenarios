### Step 4: Load Data from SQL Database

The fourth step is to load data from a SQL database using Pandas. We will use the `pd.read_sql()` method to read the data from the SQL database. For this example, we will assume that you have a SQL Server database named `sales_data` with a table named `sales`.

```python
import pandas as pd
from sqlalchemy import create_engine

# Create a SQL database engine
engine = create_engine('mssql+pyodbc://user:password@server/database?driver=SQL+Server')

# Load data from SQL database
data = pd.read_sql('SELECT * FROM sales', con=engine)

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
