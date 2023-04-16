### Step 5: Save Data to CSV File

The fifth step is to save data to a CSV file using Pandas. We will use the `pd.to_csv()` method to save the data to a CSV file.

```python
import pandas as pd

# Load data from CSV file
data = pd.read_csv('sales_data.csv')

# Save data to CSV file
data.to_csv('sales_data_cleaned.csv', index=False)
```
