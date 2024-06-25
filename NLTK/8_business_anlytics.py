
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Sales': [1000, 1500, 1200, 1800, 2000],
    'Expenses': [400, 500, 450, 600, 550]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Sample Sales Data:")
print(df.head())

# Calculate summary statistics
summary_stats = df.describe()
print("\nSummary Statistics:")
print(summary_stats)

# Plotting sales and expenses over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Date'], df['Expenses'], marker='s', label='Expenses')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.title('Sales and Expenses Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
