import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample advertising data (advertising expenses vs. sales)
data = {
    'Advertising': [100, 200, 300, 400, 500],
    'Sales': [1500, 2500, 3500, 4500, 5500]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Split the data into features (X) and target variable (y)
X = df[['Advertising']]
y = df['Sales']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Predict sales for new advertising expenses
new_expenses = [[600]]  # Example new advertising expenses
predicted_sales = model.predict(new_expenses)
print("Predicted Sales for Advertising Expenses $600:", predicted_sales[0])


print(df)
print(X)
print(y)
# Output
# Predicted Sales for Advertising Expenses $600: 6500.0