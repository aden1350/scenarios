### Step 8: Save Data to SQL Database

The eighth step is to save data to a SQL database using Pandas. We will use the `pd.to_sql()` method to save the data to the SQL database. For this example, we will assume that you have a SQL Server database named `sales_data` with a table named `sales_cleaned`.

```python
import pandas as pd
import sqlite3

# Connect to SQL database
conn = sqlite3.connect("sales_data.db")

# Load data from SQL database
data = pd.read_sql('SELECT * FROM sales', con=conn)

# Save data to SQL database
data.to_sql('sales_cleaned', con=conn, if_exists='replace', index=False)
```
