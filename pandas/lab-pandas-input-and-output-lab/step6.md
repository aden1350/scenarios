### Step 6: Save Data to Excel File

The sixth step is to save data to an Excel file using Pandas. We will use the `pd.to_excel()` method to save the data to an Excel file.

```python
# Save data to Excel file
data.to_excel('sales_data_cleaned.xlsx', index=False)
```
