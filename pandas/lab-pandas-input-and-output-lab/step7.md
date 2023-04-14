### Step 7: Save Data to JSON File

The seventh step is to save data to a JSON file using Pandas. We will use the `pd.to_json()` method to save the data to a JSON file.

```python
# Save data to JSON file
data.to_json('sales_data_cleaned.json', orient='records')
```
